---
name: sdd-report
model: sonnet
description: >-
  Use to generate a usage & metrics report of the SDD work on a project or
  feature. Auto-use when the user says "relatório", "report", "métricas",
  "quanto custou", "quanto gastei", "tokens gastos", "tempo gasto", "ROI do SDD",
  or wants to justify/analyze SDD usage after delivery. Reads local transcripts +
  SDD artifacts (nothing leaves the machine) and writes report.md.
---

# sdd-report

Gera um relatório de **esforço (tokens, tempo, custo) + qualidade/governança** do uso do SDD,
cruzando os **transcripts locais** do Claude Code com os **artefatos SDD** do repo. Emite `report.md`.

Tudo é **local**: lê só `~/.claude/projects/...` e arquivos do projeto; **não envia nada**.

## Escopo

- **Feature:** relatório de uma feature — usa a branch da feature (`feat|fix|chore/<slug>`) e
  `specs/<NNN>-<slug>/`. Grava `specs/<NNN>-<slug>/report.md`.
- **Projeto:** relatório consolidado de todas as branches/features. Grava `report.md` na raiz.
- Na dúvida, perguntar qual escopo; se houver uma feature ativa no `state.md`, assumir ela.

## Passos

1. **Esforço (determinístico).** Rodar o agregador e capturar o JSON:
   `python3 ${CLAUDE_PLUGIN_ROOT}/sdd/report/usage.py --project-dir <raiz-do-projeto> [--branch <branch-da-feature>]`
   Ele devolve, por feature/modelo/fase: turnos, tool calls, tokens (in/out/thinking/cache), tempo
   (ativo e decorrido), web calls e **custo estimado** (via `sdd/report/pricing.json`).
   - Sem Python 3, ou `transcript_files: 0` / `warning` no JSON: dizer isso no relatório e seguir só
     com a parte de qualidade (não inventar números).
2. **Qualidade & governança (dos artefatos).** Ler, quando existirem:
   - `tasks.md` → nº de tasks, quantas `done` **com evidência objetiva**, re-trabalho (reabertas/`blocked`).
   - `state.md` → histórico: checkpoints humanos, gates do `sdd-analyze`, o que foi retomado.
   - `requirements.md` → checkpoint de aprovação do pedido.
   - `design.md` → guidelines aplicadas.
   - `acceptance.md` → veredito final e conformidade com a `constitution.md`.
3. **Compor.** Preencher `${CLAUDE_PLUGIN_ROOT}/sdd/templates/report.md` com os dois lados e gravar o
   `report.md` no caminho do escopo. Derivar:
   - `hh:mm` a partir dos segundos; `R$` a partir de `US$ × fx_to_brl` (se `fx_to_brl` != null).
   - **custo por task** = custo / nº de tasks entregues.
   - **% pensar vs executar** = custo das fases de decisão (constitution, discovery, requirements,
     design, acceptance) sobre o total, vs execução (backlog, analyze, delivery) + registro (state).
4. **Ler os números, não só listar.** No resumo executivo, dizer o que a métrica significa
   (ex.: "78% do gasto foi em decisão → o erro foi decidido no texto, barato").

## Regras

- **Só reporte o que sai do agregador ou dos artefatos.** Nada de estimar tokens/tempo de cabeça.
- **Custo é sempre ESTIMATIVA** — citar `sdd/report/pricing.json` e a data (`as_of`); se o preço/plano
  mudou, o usuário edita esse arquivo. Lembrar que **cache-read é barato** e domina os tokens, então
  tokens brutos ≠ custo.
- Se um lado faltar (sem transcript, ou sem artefatos SDD), gerar o relatório com o que há e **dizer o
  que faltou** — não bloquear.
- O `report.md` é um registro auditável; deve se sustentar sozinho, sem depender da conversa.
- Não altera artefatos de outras skills; só escreve `report.md`. Não precisa de lock nem de branch dona.
