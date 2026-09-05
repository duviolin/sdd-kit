# Test Strategy

Qualidade não é "escrevi um teste" — é cobrir o comportamento certo, no nível certo, incluindo o
que dá errado. Pensamento adversarial antes de código.

## Pirâmide (proporção saudável)

- **Unit** (muitos): regra de negócio pura, rápida, isolada. A base.
- **Integração** (alguns): módulos + borda real (banco, fila, HTTP interno).
- **E2E** (poucos): fluxo do usuário ponta a ponta. Caro e lento — só o essencial.

## Por requisito, decida o nível

- Cada critério de aceite (CA) mapeia para **pelo menos um** teste automatizado.
- Escolha o nível mais barato que ainda prova o CA. Não suba pra e2e o que unit já garante.

## Teste além do caminho feliz (obrigatório)

- **Negativo:** entrada inválida, ausente, malformada → erro esperado, nada corrompido.
- **Borda:** vazio, zero, limite, duplicado, máximo/mínimo, concorrência.
- **Erro/falha:** dependência fora do ar, timeout, permissão negada.
- **Regressão:** bug reportado vira primeiro um teste que o reproduz, depois a correção.

## Não-funcionais (quando houver RN)

- Performance, segurança, acessibilidade viram **evidência objetiva** (um número, uma saída de
  ferramenta), não "parece ok".

## Qualidade do próprio teste

- Um teste prova uma afirmação observável e **falha se o comportamento quebrar**. Teste que passa
  com qualquer implementação não prova nada.

## Aplicação no SDD

- `sdd-design`: preencher a "Estratégia de testes" — nível e casos (feliz/negativo/borda) por CA.
- `sdd-delivery`: red-first (teste falhando antes do código); cobrir os casos declarados.
- `sdd-acceptance`: rodar cobertura; todo CA e todo caminho de erro provado; NFR com evidência.
