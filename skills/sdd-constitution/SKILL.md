---
name: sdd-constitution
description: >-
  Use to define or update a project's non-negotiable engineering principles that
  govern every SDD phase. Auto-use when starting SDD on a project with no
  constitution.md, or when the user says "princípios", "constituição",
  "constitution", "padrões do projeto", "regras que valem pra tudo". Creates or
  updates a project-level constitution.md.
---

# sdd-constitution

Cria/atualiza `constitution.md` na raiz do projeto: os **princípios inegociáveis** que toda
feature herda. É o documento que gateia `sdd-requirements`, `sdd-design`, `sdd-delivery` e
`sdd-acceptance`.

## Passos

1. Ler `constitution.md` se já existir (documento vivo — atualizar com bump de versão, não recriar).
2. Levantar os princípios reais: padrões de código/teste, política de erro e segurança, camadas
   permitidas/proibidas, processo (branch, revisão), restrições de negócio/plataforma. Basear-se
   em evidência do repo + decisão humana — não inventar regra que o time não segue.
3. Preencher a partir de `${CLAUDE_PLUGIN_ROOT}/sdd/templates/constitution.md`. Cada princípio deve ser
   **verificável** (dá pra dizer objetivamente se foi violado).
4. Escrever/atualizar `constitution.md` na raiz e registrar a versão no histórico.

## Regras

- Um `constitution.md` por projeto. É prescritivo (o que **sempre/nunca** fazer), diferente do
  `architecture.md`, que é descritivo (o que o sistema **é**).
- Só muda por decisão humana explícita, com bump de versão.
- Mudança aqui pode invalidar specs/planos em aberto — sinalizar quando isso acontecer.
- Próximo passo natural: `sdd-discovery` (ou direto `sdd-requirements`).
