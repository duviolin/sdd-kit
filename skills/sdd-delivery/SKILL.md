---
name: sdd-delivery
description: >-
  Use to implement an SDD feature task-by-task from the real project artifacts.
  Auto-use when the user says "implementa", "segue", "continua", "aprovado", or
  when there is a tasks.md with open tasks. Executes exactly one task per turn
  and only marks it done with objective evidence.
---

# sdd-delivery

Executa as tasks de `specs/<NNN>-<slug>/tasks.md` a partir dos artefatos reais do projeto.

## Pré-condição

- Existir `tasks.md` com tasks. Ler `constitution.md`, `requirements.md`, `design.md` e `tasks.md`.
- `sdd-analyze` já passou (consistência ok). Se não passou, rodar antes.
- Estar na branch de trabalho definida no design (`feat|fix|chore/<slug>`); criar/confirmar antes de codar.

## Ciclo (uma task por turno)

1. Escolher a próxima task `todo` sem bloqueios (respeitar ordem/dependências). Marcar `in_progress`.
2. Aplicar as guidelines do design — em especial **TDD** (`${CLAUDE_PLUGIN_ROOT}/sdd/guidelines/tdd.md`) e
   `test-strategy`: **red-first** — escreva o teste que falha (caso feliz **e** os "casos de borda/erro"
   da task) e mostre o vermelho; depois o código mínimo pro verde; depois refactor. Seguir `solid`,
   `defensive-programming`, `dry`, `kiss`, `yagni`, `clean-code`, `error-handling`, `rich-domain`,
   `secure-by-default` conforme o design indicou, sempre dentro dos princípios da `constitution.md`.
3. Rodar a verificação (testes/comando da "evidência esperada"), incluindo os casos de borda/erro.
4. Só marcar `done` com **evidência objetiva** — colar o comando + resultado em "Evidência obtida"
   (o vermelho inicial e o verde final). Sem evidência, a task fica `in_progress` ou `blocked`
   (com o motivo), nunca `done`.
5. Atualizar a tabela-resumo de `tasks.md`.

## Regras

- Uma task por turno; não pular para a próxima antes de fechar a atual com evidência.
- Não sair do escopo da task/requisitos. Necessidade nova → volta pra `sdd-requirements`/`sdd-design`, não improvisa.
- Trabalho de feature vai numa branch, não direto na `main`.
- Ao fechar a **última** task, encaminhar para `sdd-acceptance`.

## Estado (lock)

- Respeitar o protocolo do `sdd-state`: ler `state.md` antes de agir; se **outra** feature estiver `in_progress`, parar e avisar. Ao iniciar/fechar esta etapa, atualizar o bloco LOCK e o histórico.
