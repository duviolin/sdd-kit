# Defensive Code (fail fast)

Falhe alto e cedo, o mais perto possível da causa, em vez de propagar estado inválido.

## Regras práticas

- Valide entradas na borda (função pública, borda da API) e rejeite o inválido já.
- Prefira lançar um erro claro a retornar `null`/valor default silencioso que estoura depois.
- Torne estados impossíveis irrepresentáveis (tipos, invariantes no construtor).
- Mensagem de erro diz **o quê** e **por quê**, com contexto suficiente para agir.
- Trate o mundo externo (rede, arquivo, input do usuário) como hostil por padrão.

## Anti-padrões

- Engolir exceção com `catch` vazio.
- Continuar o fluxo com dado sabidamente corrompido "para não quebrar".
- Erro genérico sem contexto (`throw new Error("erro")`).

## Aplicação no SDD

- `sdd-design`: marque onde validar/rejeitar na borda.
- `sdd-delivery`: guard clauses de entrada; combine com `error-handling` e `secure-by-default`.
