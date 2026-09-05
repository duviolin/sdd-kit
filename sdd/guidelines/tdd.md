# TDD — Test-Driven Development

Todo comportamento novo ou alterado nasce de um teste que falha primeiro.

## Ciclo

1. **Red** — escreva o menor teste que falha e descreve o comportamento desejado.
2. **Green** — escreva o mínimo de código para passar.
3. **Refactor** — limpe sem mudar comportamento; os testes seguem verdes.

## Regras práticas

- Um teste prova **uma** afirmação observável. Nome descreve o comportamento, não o método.
- Teste a borda pública, não detalhes internos — refatorar não deve quebrar testes válidos.
- Bug reportado → primeiro um teste que o **reproduz**, depois a correção.
- Sem teste falhando antes, não há evidência de que o teste testa algo.

## Aplicação no SDD

- `sdd-backlog`: cada task carrega a **evidência esperada** (o teste que a fecha).
- `sdd-delivery`: só marca `done` com o teste verde colado como evidência.
- `sdd-acceptance`: cada critério de aceite deve mapear para pelo menos um teste.
