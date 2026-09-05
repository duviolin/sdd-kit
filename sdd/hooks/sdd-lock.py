#!/usr/bin/env python3
"""sdd-lock — PreToolUse hook do sdd-kit.

Trava cooperativa REFORÇADA: se existir `.sdd/lock` no projeto e a branch dona for diferente da
branch atual, bloqueia Edit/Write/MultiEdit/NotebookEdit — evitando que outra janela de contexto
sobrescreva o trabalho em andamento. É no-op em qualquer projeto sem `.sdd/lock`.

Protocolo: lê o JSON do PreToolUse no stdin. exit 0 = permite; exit 2 = bloqueia (stderr volta
para o modelo). Edições a `STATE.md` e a `.sdd/` seguem sempre liberadas (para gestão/override).
"""
import sys, os, json, time, subprocess

WRITE_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit"}
TTL_SECONDS = 8 * 3600


def allow():
    sys.exit(0)


def deny(msg):
    print(f"[sdd-lock] {msg}", file=sys.stderr)
    sys.exit(2)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        allow()

    if data.get("tool_name", "") not in WRITE_TOOLS:
        allow()

    cwd = data.get("cwd") or os.getcwd()
    lock_path = os.path.join(cwd, ".sdd", "lock")
    if not os.path.isfile(lock_path):
        allow()

    # Nunca bloquear a gestão do próprio estado/lock.
    tin = data.get("tool_input") or {}
    fp = tin.get("file_path") or tin.get("notebook_path") or ""
    if os.path.basename(fp) == "STATE.md" or (os.sep + ".sdd" + os.sep) in fp \
            or fp.endswith(os.sep + ".sdd"):
        allow()

    try:
        lock = json.load(open(lock_path))
    except Exception:
        allow()

    ts = lock.get("ts", 0)
    if ts and (time.time() - ts) > TTL_SECONDS:
        print("[sdd-lock] lock expirado (> 8h) de "
              f"{lock.get('feature')} / {lock.get('branch')} — permitindo; revise o STATE.md.",
              file=sys.stderr)
        allow()

    try:
        cur = subprocess.check_output(
            ["git", "-C", cwd, "rev-parse", "--abbrev-ref", "HEAD"],
            stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        cur = ""

    locked_branch = lock.get("branch", "")
    if locked_branch and cur and locked_branch == cur:
        allow()  # mesma feature/branch — segue o trabalho

    deny(f"trava ativa: feature '{lock.get('feature')}' na branch '{locked_branch}' "
         f"(dono {lock.get('owner')}). Você está em '{cur or 'sem git'}'. "
         f"Use sdd-state (release) ou troque para a branch da feature. "
         f"Edições a STATE.md/.sdd continuam liberadas.")


if __name__ == "__main__":
    main()
