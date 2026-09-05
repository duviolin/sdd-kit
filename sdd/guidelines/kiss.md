# KISS — Keep It Simple

A solução mais simples que resolve o problema é a certa. Complexidade se paga em manutenção.

## Regras práticas

- Prefira código óbvio a código "esperto". Legibilidade > concisão.
- Menos camadas, menos indireção, menos configuração do que o problema exige.
- Uma função faz uma coisa; se precisa de comentário pra explicar "o quê", provavelmente é grande demais.
- Escolha a estrutura de dados/algoritmo mais simples que atende o requisito real.

## Anti-padrões

- Padrão de projeto aplicado "por elegância" sem necessidade.
- Generalização especulativa ("e se um dia precisar de N?") — ver `yagni`.
- Encadeamento e metaprogramação que ninguém do time consegue depurar.

## Aplicação no SDD

- `sdd-design`: 1 recomendação simples, não um catálogo de opções.
- `sdd-delivery`: se a implementação ficou complexa, reveja se o escopo da task inchou.
