# DESIGN — <título da feature>

- **ID:** <NNN>-<slug>
- **Status:** draft | ready | done
- **Requirements:** ./requirements.md (aprovado em <YYYY-MM-DD>)
- **Branch:** <feat|fix|chore/slug>
- **Data:** <YYYY-MM-DD>

## Estratégia técnica

<Como resolver. A abordagem escolhida e por quê (1 recomendação, não um catálogo).>
<Respeita a `CONSTITUTION.md`? Aponte quais princípios (P1, P2...) guiam a escolha.>

## Impacto no código

| Área / arquivo | Mudança | Motivo |
|----------------|---------|--------|
| <path>         | <criar/editar/remover> | <requisito> |

## Dependências

- <libs, serviços, features precedentes, migrações, flags>

## Riscos

- <risco> → <mitigação>

## Guidelines aplicáveis

<Quais guidelines do sdd-kit guiam esta implementação e onde importam.>
Ex.: `tdd` (todo comportamento novo), `solid`, `defensive-programming` na borda de entrada,
`error-handling` nos fluxos de falha, `secure-by-default` no que toca dado externo.
Disponíveis: `tdd`, `solid`, `defensive-programming`, `rich-domain`, `dry`, `kiss`, `yagni`,
`clean-code`, `error-handling`, `secure-by-default`, `code-review`, `test-strategy`.

## Ordem de execução

1. <passo — vira task>
2. <...>

## Estratégia de testes

Por critério de aceite: nível de teste + casos além do caminho feliz (ver `test-strategy`).

| CA  | Nível (unit/integração/e2e) | Casos (feliz / negativo / borda / erro) |
|-----|-----------------------------|-----------------------------------------|
| CA1 | <...>                       | <...>                                   |

- NFR (perf/segurança/acessibilidade): <como cada um será provado com evidência objetiva>.

## Validação planejada

- Como cada critério de aceite será provado (teste, comando, saída esperada) e a
  **cobertura** a atingir. Isto vira a base do `sdd-acceptance`.
