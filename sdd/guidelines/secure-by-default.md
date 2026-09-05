# Secure by Default

Segurança é o estado padrão, não um extra opcional. O caminho fácil deve ser o caminho seguro.

## Regras práticas

- **Nunca confie na entrada**: valide/sanitize tudo que vem de fora (usuário, rede, arquivo).
- Queries parametrizadas sempre (anti SQL injection); escape saída por contexto (anti XSS).
- Segredos fora do código e do log — em variável de ambiente/secret manager.
- Menor privilégio: cada componente só acessa o que precisa.
- Negue por padrão; libere explicitamente (allowlist > denylist).
- Não invente cripto — use bibliotecas estabelecidas para hash, auth e tokens.

## Anti-padrões

- Concatenar input em SQL/HTML/shell.
- Credencial commitada ou impressa em log.
- Verificação de autorização só no front-end.

## Aplicação no SDD

- `sdd-requirements`: requisitos não-funcionais de segurança viram CA verificável.
- `sdd-delivery`/`sdd-acceptance`: caminho de abuso testado; sem segredo no diff.
