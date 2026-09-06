---
name: sdd-design
description: >-
  Use after a requirements doc is approved to design the technical plan. Auto-use
  when the user approves requirements and says "plano", "plan", "design", "como
  vamos fazer", or asks to move an approved spec toward implementation. Converts
  approved requirements into design.md; refuses to run if not yet approved.
---

# sdd-design

Converte um `requirements.md` **aprovado** em `specs/<NNN>-<slug>/design.md`.

## Pré-condição

- O `requirements.md` do mesmo `<NNN>-<slug>` deve estar `Status: approved`.
- Se estiver `awaiting_approval`/`draft` → **parar** e pedir a aprovação antes (não planejar).

## Passos

1. Ler `requirements.md`, a `constitution.md` e o `architecture.md` do projeto.
2. Preencher a partir de `${CLAUDE_PLUGIN_ROOT}/sdd/templates/design.md`: estratégia técnica (1 recomendação,
   não catálogo), impacto por arquivo, dependências, riscos+mitigação, ordem de execução,
   validação planejada (como cada CA será provado), e a **branch** de trabalho (`feat|fix|chore/<slug>`).
3. Garantir que a estratégia **respeita a `constitution.md`** — citar quais princípios guiam a escolha.
4. Preencher a **Estratégia de testes** (nível + casos de borda/erro por CA) — ver `test-strategy`.
5. Citar as guidelines relevantes de `${CLAUDE_PLUGIN_ROOT}/sdd/guidelines/` e **onde** importam
   (`tdd`, `test-strategy`, `solid`, `defensive-programming`, `rich-domain`, `dry`, `kiss`, `yagni`,
   `clean-code`, `error-handling`, `secure-by-default`, `code-review`).
6. Gravar `design.md` com `Status: ready`.

## Regras

- A "Validação planejada" é a base do `sdd-acceptance` — cada critério de aceite mapeado a uma prova.
- Não incluir trabalho fora do escopo dos requisitos. Se surgir necessidade nova, volta pra `sdd-requirements`.
- Próximo passo natural: `sdd-backlog`.

## Estado (lock)

- Respeitar o protocolo do `sdd-state`: ler `state.md` antes de agir; se **outra** feature estiver `in_progress`, parar e avisar. Ao iniciar/fechar esta etapa, atualizar o bloco LOCK e o histórico.
