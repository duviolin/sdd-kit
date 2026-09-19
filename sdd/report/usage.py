#!/usr/bin/env python3
"""Agrega uso de tokens/tempo/custo de um projeto SDD a partir dos transcripts locais
do Claude Code (~/.claude/projects/<cwd-manglada>/*.jsonl).

Atribui o gasto por:
  - feature  (campo gitBranch de cada turno)
  - modelo   (campo message.model — mapeia pra fase: Opus pensa, Sonnet executa, Haiku anota)
  - fase SDD (detectada pela última skill sdd-* ativada na sessão)

Tudo é LOCAL: lê só arquivos da máquina, não envia nada pra lugar nenhum.
Emite um JSON no stdout que a skill sdd-report transforma em report.md.

Uso:
  python3 usage.py --project-dir /caminho/do/projeto [--branch feat/x] [--pricing pricing.json]
  python3 usage.py --project-dir . --transcripts-dir ~/.claude/projects/-Users-...  # override
"""
import argparse
import glob
import json
import os
import sys
from collections import defaultdict
from datetime import datetime

# skill sdd-* -> fase (chave curta usada no relatório)
PHASE_OF_SKILL = {
    "sdd-constitution": "constitution",
    "sdd-discovery": "discovery",
    "sdd-requirements": "requirements",
    "sdd-design": "design",
    "sdd-backlog": "backlog",
    "sdd-analyze": "analyze",
    "sdd-delivery": "delivery",
    "sdd-acceptance": "acceptance",
    "sdd-state": "state",
    "sdd-report": "report",
}
IDLE_GAP_CAP = 300  # s: intervalos maiores entre turnos contam como "ocioso" (não somam no tempo ativo)


def mangle(cwd):
    """~/.claude/projects usa o caminho absoluto do cwd com '/' -> '-'."""
    return cwd.replace("/", "-")


def parse_ts(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def new_tokens():
    return {
        "input": 0,
        "output": 0,
        "thinking": 0,
        "cache_read": 0,
        "cache_write_5m": 0,
        "cache_write_1h": 0,
    }


def add_tokens(dst, src):
    for k in dst:
        dst[k] += src.get(k, 0)


def tokens_from_usage(u):
    t = new_tokens()
    t["input"] = u.get("input_tokens", 0) or 0
    t["output"] = u.get("output_tokens", 0) or 0
    t["thinking"] = (u.get("output_tokens_details") or {}).get("thinking_tokens", 0) or 0
    t["cache_read"] = u.get("cache_read_input_tokens", 0) or 0
    cc = u.get("cache_creation") or {}
    if cc:
        t["cache_write_5m"] = cc.get("ephemeral_5m_input_tokens", 0) or 0
        t["cache_write_1h"] = cc.get("ephemeral_1h_input_tokens", 0) or 0
    else:
        # fallback: só o total de cache_creation -> trata como 5min (o mais comum/barato)
        t["cache_write_5m"] = u.get("cache_creation_input_tokens", 0) or 0
    return t


def price_for_model(pricing, model):
    """Preço por modelo: match exato, senão por família (claude-opus*, claude-sonnet*, claude-haiku*)."""
    models = pricing.get("models", {})
    if model in models:
        return models[model], model
    for fam in ("claude-opus", "claude-sonnet", "claude-haiku", "claude-fable"):
        if model and model.startswith(fam):
            key = fam + "*"
            if key in models:
                return models[key], key
    return None, None


def cost_usd(pricing, model, tok):
    p, _ = price_for_model(pricing, model)
    if not p:
        return None  # sem preço -> reporta tokens, custo fica "n/d"
    per = 1_000_000.0
    return (
        tok["input"] * p.get("input", 0)
        + tok["output"] * p.get("output", 0)
        + tok["cache_read"] * p.get("cache_read", 0)
        + tok["cache_write_5m"] * p.get("cache_write_5m", 0)
        + tok["cache_write_1h"] * p.get("cache_write_1h", 0)
    ) / per


def load_pricing(path):
    if path and os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    return {"currency": "USD", "fx_to_brl": None, "models": {}, "note": "sem tabela de preços"}


def iter_entries(files):
    for f in files:
        try:
            with open(f, errors="ignore", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        yield json.loads(line)
                    except Exception:
                        continue
        except OSError:
            continue


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project-dir", default=".", help="raiz do projeto-alvo (default: cwd)")
    ap.add_argument("--branch", default=None, help="filtra uma feature (gitBranch); default: todas")
    ap.add_argument("--transcripts-dir", default=None, help="override do dir de transcripts")
    ap.add_argument("--pricing", default=None, help="pricing.json (default: ao lado deste script)")
    args = ap.parse_args()

    cwd = os.path.abspath(os.path.expanduser(args.project_dir))
    if args.transcripts_dir:
        tdir = os.path.abspath(os.path.expanduser(args.transcripts_dir))
    else:
        tdir = os.path.join(os.path.expanduser("~/.claude/projects"), mangle(cwd))
    pricing_path = args.pricing or os.path.join(os.path.dirname(os.path.abspath(__file__)), "pricing.json")
    pricing = load_pricing(pricing_path)

    files = sorted(glob.glob(os.path.join(tdir, "*.jsonl")))

    # acumuladores por branch
    def blank_branch():
        return {
            "turns": 0,
            "tool_calls": 0,
            "sessions": set(),
            "tokens": new_tokens(),
            "cost_usd": 0.0,
            "unpriced": False,
            "by_model": defaultdict(lambda: {"turns": 0, "tokens": new_tokens(), "cost_usd": 0.0}),
            "by_phase": defaultdict(lambda: {"turns": 0, "tokens": new_tokens(), "cost_usd": 0.0}),
            "web": {"search": 0, "fetch": 0},
            # tempo: por sessão -> (min_ts, max_ts, prev_ts, active_seconds)
            "_time": defaultdict(lambda: {"min": None, "max": None, "prev": None, "active": 0.0}),
        }

    branches = defaultdict(blank_branch)
    seen_uuid = set()
    session_phase = {}  # sessionId -> fase corrente

    for e in iter_entries(files):
        etype = e.get("type")
        sid = e.get("sessionId") or "?"
        msg = e.get("message") or {}
        content = msg.get("content")

        # 1) detecta ativação de skill sdd-* (define a fase corrente da sessão)
        if isinstance(content, list):
            for b in content:
                if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "Skill":
                    sk = (b.get("input") or {}).get("skill")
                    if sk in PHASE_OF_SKILL:
                        session_phase[sid] = PHASE_OF_SKILL[sk]

        # 2) só turnos de assistant com usage entram na contagem
        if etype != "assistant" or "usage" not in msg:
            continue
        uid = e.get("uuid")
        if uid and uid in seen_uuid:
            continue
        if uid:
            seen_uuid.add(uid)

        branch = e.get("gitBranch") or "(sem branch)"
        if args.branch and branch != args.branch:
            continue
        model = msg.get("model") or "(desconhecido)"
        phase = session_phase.get(sid, "(fora de skill)")
        tok = tokens_from_usage(msg["usage"])
        c = cost_usd(pricing, model, tok)
        has_tok = any(tok[k] for k in tok)
        if c is None:
            if has_tok:
                br0 = branches[branch]
                br0["unpriced"] = True  # turno com tokens reais e sem preço na tabela
            c = 0.0

        br = branches[branch]
        br["turns"] += 1
        br["sessions"].add(sid)
        add_tokens(br["tokens"], tok)
        br["cost_usd"] += c

        bm = br["by_model"][model]
        bm["turns"] += 1
        add_tokens(bm["tokens"], tok)
        bm["cost_usd"] += c

        bp = br["by_phase"][phase]
        bp["turns"] += 1
        add_tokens(bp["tokens"], tok)
        bp["cost_usd"] += c

        if isinstance(content, list):
            for b in content:
                if isinstance(b, dict) and b.get("type") == "tool_use":
                    br["tool_calls"] += 1
        stu = msg["usage"].get("server_tool_use") or {}
        br["web"]["search"] += stu.get("web_search_requests", 0) or 0
        br["web"]["fetch"] += stu.get("web_fetch_requests", 0) or 0

        # tempo
        ts = parse_ts(e.get("timestamp"))
        if ts:
            st = br["_time"][sid]
            if st["min"] is None or ts < st["min"]:
                st["min"] = ts
            if st["max"] is None or ts > st["max"]:
                st["max"] = ts
            if st["prev"] is not None:
                delta = (ts - st["prev"]).total_seconds()
                if 0 <= delta <= IDLE_GAP_CAP:
                    st["active"] += delta
            st["prev"] = ts

    # serializa
    def finalize(br):
        elapsed = 0.0
        active = 0.0
        first = None
        last = None
        for st in br["_time"].values():
            if st["min"] and st["max"]:
                elapsed += (st["max"] - st["min"]).total_seconds()
                first = st["min"] if first is None or st["min"] < first else first
                last = st["max"] if last is None or st["max"] > last else last
            active += st["active"]
        out = {
            "turns": br["turns"],
            "tool_calls": br["tool_calls"],
            "sessions": len(br["sessions"]),
            "tokens": br["tokens"],
            "cost_usd": round(br["cost_usd"], 4),
            "has_unpriced_turns": br["unpriced"],
            "time": {
                "elapsed_seconds": round(elapsed, 1),
                "active_seconds": round(active, 1),
                "first": first.isoformat() if first else None,
                "last": last.isoformat() if last else None,
            },
            "web": br["web"],
            "by_model": {
                m: {"turns": v["turns"], "tokens": v["tokens"], "cost_usd": round(v["cost_usd"], 4)}
                for m, v in sorted(br["by_model"].items())
            },
            "by_phase": {
                p: {"turns": v["turns"], "tokens": v["tokens"], "cost_usd": round(v["cost_usd"], 4)}
                for p, v in sorted(br["by_phase"].items())
            },
        }
        return out

    result_branches = {b: finalize(v) for b, v in sorted(branches.items())}

    # totais
    totals = {
        "turns": sum(v["turns"] for v in result_branches.values()),
        "tool_calls": sum(v["tool_calls"] for v in result_branches.values()),
        "cost_usd": round(sum(v["cost_usd"] for v in result_branches.values()), 4),
        "tokens": new_tokens(),
    }
    for v in result_branches.values():
        add_tokens(totals["tokens"], v["tokens"])

    fx = pricing.get("fx_to_brl")
    out = {
        "meta": {
            "project_dir": cwd,
            "transcripts_dir": tdir,
            "transcript_files": len(files),
            "generated_at": datetime.now().astimezone().isoformat(),
            "branch_filter": args.branch,
        },
        "pricing": {
            "currency": pricing.get("currency", "USD"),
            "fx_to_brl": fx,
            "source_note": pricing.get("note"),
            "as_of": pricing.get("as_of"),
        },
        "totals": totals,
        "branches": result_branches,
    }
    if not files:
        out["meta"]["warning"] = (
            "Nenhum transcript encontrado em transcripts_dir. Confira o caminho ou rode "
            "a partir da raiz do projeto (o dir é derivado do caminho absoluto do cwd)."
        )
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
