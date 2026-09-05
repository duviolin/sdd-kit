# SOLID

Cinco princípios para código orientado a objetos sustentável.

- **S — Single Responsibility:** uma classe/módulo tem um único motivo para mudar.
- **O — Open/Closed:** aberto para extensão, fechado para modificação — estenda sem editar o núcleo estável.
- **L — Liskov Substitution:** subtipos devem substituir o tipo base sem quebrar expectativas.
- **I — Interface Segregation:** muitas interfaces específicas > uma interface gorda; ninguém depende do que não usa.
- **D — Dependency Inversion:** dependa de abstrações, não de implementações concretas; injete dependências.

## Cheiros que violam

- Classe que faz I/O, regra de negócio e formatação juntas (S).
- `switch`/`if` por tipo que cresce a cada feature nova (O).
- Subclasse que lança "não suportado" em método herdado (L).
- Implementar interface e deixar metade dos métodos vazios (I).
- `new ConcreteThing()` no meio da regra de negócio (D).

## Aplicação no SDD

- `sdd-design`: escolha de camadas/abstrações justificada por estes princípios.
- `sdd-delivery`: refatore para SOLID no passo de refactor do TDD, sem inflar escopo.
