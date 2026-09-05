# YAGNI — You Aren't Gonna Need It

Não construa hoje o que só o "talvez futuro" pede. Implemente o requisito atual, nada além.

## Regras práticas

- Código para um caso que ninguém pediu é custo garantido por benefício hipotético.
- Prefira adicionar quando a necessidade real aparecer (com teste que a prove) a antecipar.
- Ponto de extensão só quando há um segundo caso concreto, não um imaginado.

## Anti-padrões

- Flags/configs "para flexibilidade" sem consumidor.
- Camada de abstração com uma única implementação "por precaução".
- Parâmetros e branches para cenários que os requisitos não descrevem.

## Aplicação no SDD

- `sdd-requirements`/`sdd-design`: o escopo "fora" dos requisitos delimita o que **não** entra.
- `sdd-delivery`: se surgir necessidade nova, volta pra `sdd-requirements` — não improvisa na task. Equilibra `dry`.
