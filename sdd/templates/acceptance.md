# ACCEPTANCE — <título da feature>

- **ID:** <NNN>-<slug>
- **Veredito:** aprovado | reprovado | aprovado-com-ressalvas
- **Branch:** <feat|fix|chore/slug>
- **Validado em:** <YYYY-MM-DD>
- **Validador:** <quem/agente>

> Veredito final da entrega, baseado em artefatos versionados + diff da
> branch + evidências persistidas. Gerado por `sdd-acceptance`.

## Escopo entregue vs requisitos

| Requisito | Critério | Coberto? | Evidência |
|-----------|----------|----------|-----------|
| R1        | CA1      | ✅/❌     | <teste/saída/diff> |

## Cobertura de testes

- <o que foi testado, tipo (unit/integração/e2e), resultado>

## Diff da branch

- <arquivos tocados coerentes com o design? algo fora do escopo?>
- Comando: `git diff <base>...<branch> --stat`

## Conformidade com a CONSTITUTION

- <a entrega respeitou os princípios do projeto? alguma violação?>

## Ressalvas / débito técnico

- <o que ficou de fora, com follow-up>

## Conclusão

<Por que aprovado/reprovado. Se reprovado, o que falta para reabrir.>
