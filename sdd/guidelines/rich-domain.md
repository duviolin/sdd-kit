# Rich Domain (evitar classes anêmicas)

Uma classe anêmica é só um saco de getters/setters, sem comportamento. A regra de negócio
vaza para "serviços" que manipulam o estado de fora — o oposto de OO.

## Sintoma

```
class Conta { double saldo; getSaldo(); setSaldo(v); }
class ContaService { sacar(c, v){ if (c.getSaldo()>=v) c.setSaldo(c.getSaldo()-v); } }
```

A `Conta` não protege seu próprio invariante; qualquer um faz `setSaldo(-999)`.

## Rico

```
class Conta {
  private saldo;
  sacar(valor) {
    if (valor <= 0) throw ...;
    if (valor > saldo) throw SaldoInsuficiente;
    saldo -= valor;
  }
}
```

## Regras práticas

- Coloque a regra **junto** do dado que ela protege (tell, don't ask).
- Invariantes garantidos no construtor e nos métodos, não em serviços externos.
- Setters públicos que quebram invariante são cheiro de anemia.

## Aplicação no SDD

- `sdd-design`/`sdd-delivery`: modele comportamento no domínio; serviços orquestram, não contêm a regra.
