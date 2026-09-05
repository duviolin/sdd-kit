# Code Review

Toda mudança passa por revisão antes de entrar. Revisão é sobre o código, nunca sobre a pessoa.

## O que o autor entrega

- Diff pequeno e coeso (uma intenção por PR); descrição liga a `requirements`/`tasks`.
- Testes junto da mudança; caminho feliz e de erro cobertos.
- Sem ruído: nada de arquivo gerado, segredo, código comentado ou TODO órfão.

## O que o revisor checa

- **Correção:** faz o que os requisitos pedem? cobre os critérios de aceite?
- **Escopo:** nada fora do que a task/requisitos define no diff.
- **Legibilidade e guidelines:** `clean-code`, `solid`, `dry`, `kiss`, `error-handling`, `secure-by-default`.
- **Testes:** provam o comportamento, não detalhes internos frágeis.
- Comentário aponta o problema **e** sugere caminho; distingue "bloqueante" de "opcional".

## Aplicação no SDD

- `sdd-delivery`: cada task fecha com evidência — facilita a revisão.
- `sdd-acceptance`: o `acceptance.md` consolida a revisão final contra o diff da branch.
