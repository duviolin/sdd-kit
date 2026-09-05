# Clean Code (nomes e legibilidade)

Código é lido muitas mais vezes do que escrito. Otimize para quem vai ler depois.

## Regras práticas

- Nomes revelam intenção: `saldoDisponivel`, não `s` ou `tmp`. Função nomeia o que faz.
- Nome do tamanho do escopo: variável de loop curta ok; símbolo público, descritivo.
- Sem números/strings mágicos — extraia constante nomeada.
- Função curta, um nível de abstração por função; evite flags booleanas que criam dois comportamentos.
- Comentário explica **por quê**, não **o quê** (o "o quê" é o próprio código).
- Formatação e estilo consistentes com o resto do repositório.

## Anti-padrões

- Nomes genéricos (`data`, `info`, `manager`, `helper`, `util`) sem significado.
- Comentário que repete o código ou que mente porque ficou desatualizado.
- Função que faz três coisas e precisa de comentários-seção internos.

## Aplicação no SDD

- `sdd-delivery`: nomes e legibilidade entram no passo de refactor do TDD.
- `sdd-acceptance`: código ilegível é ressalva, mesmo com testes verdes.
