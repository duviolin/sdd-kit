---
name: sdd-discovery
description: >-
  Use to map or refresh a project's real technical architecture before speccing
  work. Auto-use when onboarding into an unfamiliar repo, when the user asks
  about "arquitetura", componentes, dependências, decisões técnicas, or when a
  spec/plan needs a current architectural baseline. Creates/updates a
  project-level ARCHITECTURE.md.
---

# sdd-discovery

Cria/atualiza `ARCHITECTURE.md` na raiz do projeto: visão técnica **real e atual** (não aspiracional).

## Passos

1. Ler `ARCHITECTURE.md` se já existir (é documento vivo — atualizar, não recriar do zero).
2. Explorar o projeto real: estrutura de pastas, manifestos de deps, entrypoints, integrações,
   camadas. Basear-se em evidência do código, não em suposição.
3. Preencher a partir do template `${CLAUDE_PLUGIN_ROOT}/sdd/templates/ARCHITECTURE.md`:
   componentes, integrações externas, dependências, fluxos-chave, decisões, restrições/convenções.
4. Escrever/atualizar `ARCHITECTURE.md` na raiz (ou em `docs/` se o projeto já concentra docs lá).

## Regras

- Um `ARCHITECTURE.md` por projeto (não por feature). Feature vive em `specs/<NNN>-<slug>/`.
- É **descritivo** (o que o sistema é). O que é **prescritivo** (regra inegociável) vive na
  `CONSTITUTION.md` — não misturar os dois.
- Registrar **decisões** e **restrições** — são o que specs/planos futuros precisam respeitar.
- Não inventar arquitetura desejada; descrever a que existe, marcando gaps como tal.
- Próximo passo natural: `sdd-requirements`.
