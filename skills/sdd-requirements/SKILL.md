---
name: sdd-requirements
description: >-
  Auto-use when the user wants a new feature, product/behavior change, API or
  contract change, or says anything like "quero", "preciso", "vamos fazer",
  "feature", "spec", "nova tela", "novo endpoint" — even without naming this
  skill. Turns a story/description/ticket/code into a versioned requirements
  doc, then STOPS for human approval before any design or code.
---

# sdd-requirements

Transforma demanda (história, descrição, ticket, bug, código) em `specs/<NNN>-<slug>/requirements.md`.

## Passos

1. Ler `CONSTITUTION.md` (princípios que a feature herda) e `ARCHITECTURE.md` se existirem. Se o
   repo for novo/desconhecido e isso ajudar, sugerir `sdd-constitution` e/ou `sdd-discovery` antes.
2. Definir `<slug>` (kebab curto do título) e `<NNN>`: varrer `specs/`, pegar o maior número
   existente + 1, com 3 dígitos (`001`, `002`…). Criar a pasta `specs/<NNN>-<slug>/`.
3. Preencher a partir de `${CLAUDE_PLUGIN_ROOT}/sdd/templates/requirements.md`: problema, escopo (dentro/fora),
   requisitos em **notação EARS**, critérios de aceite (Dado/Quando/Então), premissas, dúvidas,
   rastreabilidade.
4. **Clarify:** varrer o documento por ambiguidade e fazer as perguntas de decisão humana que
   faltarem — não preencher dúvida crítica com achismo. Repetir até não restar ambiguidade bloqueante.
5. Rodar o **checklist de qualidade** do rodapé do template (EARS sem ambiguidade, todo CA
   verificável, escopo-fora preenchido, nada contra a `CONSTITUTION.md`, zero detalhe de implementação).
6. Gravar `requirements.md` com `Status: awaiting_approval`.

## Gate (obrigatório)

- Resumir em 5–10 linhas + critérios e **pedir aprovação humana explícita**.
- **NÃO** gerar design, NÃO criar branch, NÃO codar neste turno.
- Só após um "aprovado"/"segue"/"implementa" do humano, mudar `Status: approved` e seguir para `sdd-design`.

## Regras

- Critério de aceite tem que ser verificável (vira teste/evidência lá no `sdd-acceptance`).
- Escopo "fora" explícito evita creep.
- Se a demanda já tem número/slug (retomada), atualizar o documento existente em vez de duplicar.

## Estado (lock)

- Respeitar o protocolo do `sdd-state`: ler `STATE.md` antes de agir; se **outra** feature estiver `in_progress`, parar e avisar. Ao iniciar/fechar esta etapa, atualizar o bloco LOCK e o histórico.
