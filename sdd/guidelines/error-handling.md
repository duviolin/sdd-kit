# Error Handling

Erros são parte do contrato do código, não um detalhe. Trate-os de forma explícita e previsível.

## Regras práticas

- Capture o erro **onde há informação para decidir** o que fazer — não cedo demais, não tarde demais.
- Erros específicos > genéricos: tipos/classes de erro que o chamador consegue distinguir.
- Não perca contexto: propague causa original (`cause`/wrapping), não engula o stack.
- Diferencie erro esperado (regra de negócio: saldo insuficiente) de inesperado (bug/infra).
- Libere recursos de forma garantida (`finally`/`defer`/`with`/RAII).
- Log com contexto acionável; nunca logue segredo/PII.

## Anti-padrões

- `catch` vazio ou que só faz `log` e segue com estado inválido.
- Usar exceção para fluxo de controle normal.
- Mensagem para o usuário vazando stack trace ou detalhe interno.

## Aplicação no SDD

- `sdd-design`: defina a estratégia de erro (tipos, borda de captura) por fluxo.
- `sdd-delivery`: teste os caminhos de erro, não só o feliz. Combina com `defensive-programming`.
