---
name: sdd-backlog
description: >-
  Use to break an approved design into executable, verifiable tasks. Auto-use
  when the user says "tasks", "tarefas", "backlog", "quebra o plano" for a
  feature that already has a design.md. Produces tasks.md with per-task origin,
  expected evidence, status, blockers and parallel markers.
---

# sdd-backlog

Quebra o `design.md` de `specs/<NNN>-<slug>/` em `tasks.md`.

## Pré-condição

- Existir `design.md` (`Status: ready`) para o mesmo `<NNN>-<slug>`.

## Passos

1. Ler `design.md` (e `requirements.md` para rastreio de critérios).
2. Para cada passo da ordem de execução, criar uma task a partir de `${CLAUDE_PLUGIN_ROOT}/sdd/templates/tasks.md`:
   - **Origem** (passo do design / requisito, R1/CA1),
   - **Fazer** (ação concreta),
   - **Evidência esperada** (o teste/saída/diff que fecha a task),
   - **Bloqueios** e dependências entre tasks,
   - **Status:** `todo`.
3. Marcar `[P]` nas tasks que podem rodar em paralelo (sem dependência entre si).
4. Cada task deve ser pequena o bastante para caber num turno de implementação e ter
   evidência objetiva de conclusão. Preencher a tabela-resumo (task ↔ critérios cobertos).
5. Gravar `tasks.md`.

## Regras

- Toda task rastreia de volta a um requisito/critério — nada órfão.
- Ordem respeita dependências.
- Próximo passo natural: `sdd-analyze` (gate de consistência antes de implementar).

## Estado (lock)

- Respeitar o protocolo do `sdd-state`: ler `state.md` antes de agir; se **outra** feature estiver `in_progress`, parar e avisar. Ao iniciar/fechar esta etapa, atualizar o bloco LOCK e o histórico.
