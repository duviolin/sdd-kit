# CONSTITUTION — <nome do projeto>

- **Status:** living document
- **Versão:** v1
- **Atualizado:** <YYYY-MM-DD>

> Princípios **inegociáveis** deste projeto. Governam toda a trilha SDD: `sdd-requirements`,
> `sdd-design`, `sdd-delivery` e `sdd-acceptance` devem respeitar e citar o que estiver aqui.
> Só muda por **decisão humana explícita**, com bump de versão registrado abaixo.

## Princípios

- **P1 —** <regra inegociável, verificável. Ex.: "toda regra de negócio nasce de um teste (TDD)">
- **P2 —** <...>
- **P3 —** <...>

## Padrões de código

- <linguagem, formatação, linter, convenção de nomes — o que é obrigatório>
- Guidelines aplicáveis por padrão: <ex.: `clean-code`, `solid`, `dry`, `kiss`>.

## Testes (piso de QA — inegociável)

- **Cobertura mínima:** <ex.: 80% linhas / 100% da regra de negócio nova>. Comando: `<cmd de cobertura>`.
- **Tipos obrigatórios:** <ex.: unit em toda regra; integração na borda de I/O>. Ver `test-strategy`.
- **Sempre testar:** caminho feliz **e** negativo/borda/erro. Bug → teste que reproduz primeiro.
- **Não faz merge sem:** todos os CA provados, caminhos de erro cobertos, NFR com evidência objetiva.

## Erros & segurança

- <política de erro padrão (`error-handling`, `defensive-programming`)>
- <regras de segurança inegociáveis (`secure-by-default`): segredo fora do código, input não confiável...>

## Arquitetura & camadas

- <camadas/dependências permitidas e **proibidas**; o que specs/planos não podem violar>

## Processo

- <branch (`feat|fix|chore/<slug>`), revisão (`code-review`), o que bloqueia merge>

## Restrições

- <limites de negócio/legais/plataforma que toda feature herda>

---

## Histórico de versões

| Versão | Data | Mudança | Quem |
|--------|------|---------|------|
| v1     | <YYYY-MM-DD> | criação | <quem> |
