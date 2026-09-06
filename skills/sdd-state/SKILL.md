---
name: sdd-state
description: >-
  Manages the project's single execution state and lock. Auto-use when starting,
  pausing, resuming or finishing SDD work, when the user says "onde paramos",
  "retomar", "status", "trava", "lock", "o que está rodando", or when any SDD
  skill needs to know what is in progress. Reads/updates state.md and .sdd/lock
  and enforces one active feature at a time.
---

# sdd-state

Mantém a **fonte única de execução** do projeto: `state.md` (dashboard + histórico, na raiz) e
`.sdd/lock` (trava reforçada pelo hook `sdd-lock`). É o que responde "onde paramos" e impede duas
janelas de contexto de se sobrescreverem.

## Ações

- **status / onde paramos:** ler `state.md`; dizer feature, etapa, branch, status e a próxima ação.
- **acquire (iniciar):** só se `Status: free` (ou lock ausente/expirado). Escrever `.sdd/lock` (JSON:
  `feature`, `branch`, `owner`, `ts` epoch) e o bloco LOCK do `state.md` como `in_progress`; registrar
  `iniciado`. Se já houver **outra** feature `in_progress`, **parar e avisar** — não começar.
- **update:** avançar etapa/task no bloco LOCK e `Atualizado`; registrar a transição no histórico.
- **pause / block:** mudar `Status` e registrar o motivo (não libera o lock).
- **release (concluir/liberar):** `Status: free`, limpar o bloco LOCK, remover `.sdd/lock`, registrar
  `concluído`/`liberado`.

## Regras

- **Uma feature ativa por vez.** Nada começa enquanto outra estiver `in_progress`.
- `state.md` e `.sdd/lock` são a verdade entre janelas — **releia sempre antes de agir**.
- Lock com `ts` > 8h pode estar expirado; **confirmar com o humano** antes de sobrescrever.
- Criar `state.md` a partir de `${CLAUDE_PLUGIN_ROOT}/sdd/templates/state.md` se não existir.
- A trava é reforçada pelo hook `sdd-lock` (nega Edit/Write fora da branch dona). Edições a
  `state.md` e `.sdd/` seguem liberadas para permitir gestão/override.
