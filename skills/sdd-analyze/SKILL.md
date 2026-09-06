---
name: sdd-analyze
description: >-
  Use to cross-check consistency across requirements, design and tasks before
  implementing. Auto-use when tasks.md is ready, or the user says "analisa",
  "analyze", "checa consistência", "revisa antes de codar". A cheap gate that
  blocks delivery if artifacts disagree. Reports findings; does not write code.
---

# sdd-analyze

Gate de consistência entre `requirements.md`, `design.md` e `tasks.md` de `specs/<NNN>-<slug>/`,
antes de gastar execução em `sdd-delivery`. Não escreve código nem novos artefatos — reporta.

## Pré-condição

- Existir `tasks.md` para o `<NNN>-<slug>`.

## Passos

1. Ler `constitution.md` (se houver), `requirements.md`, `design.md` e `tasks.md`.
2. Checar cobertura e coerência:
   - **Requisito → design:** todo requisito tem tratamento no design?
   - **CA → task:** todo critério de aceite tem ao menos uma task que o prova? Nada órfão.
   - **Task → origem:** toda task rastreia a um passo do design / requisito? Nada inventado.
   - **Escopo:** nada no design/tasks está no "Fora (explicitamente)" dos requisitos.
   - **Constitution:** design e tasks respeitam os princípios do projeto?
   - **Contradições:** dependências de task coerentes; ordem viável; sem conflito entre artefatos.
3. Emitir veredito: **consistente** ou **inconsistente** com a lista exata do que corrigir.

## Regras

- Inconsistente → **parar**. Corrigir na skill de origem (`sdd-requirements`/`sdd-design`/
  `sdd-backlog`) antes de implementar. Não seguir para `sdd-delivery` com o gate vermelho.
- Consistente → liberar `sdd-delivery`.

## Estado (lock)

- Respeitar o protocolo do `sdd-state`: ler `state.md` antes de agir; se **outra** feature estiver `in_progress`, parar e avisar. Ao iniciar/fechar esta etapa, atualizar o bloco LOCK e o histórico.
