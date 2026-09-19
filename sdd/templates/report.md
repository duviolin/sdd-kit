# REPORT — <título da feature ou "projeto <nome>">

- **Escopo:** feature <NNN>-<slug> | projeto inteiro
- **Branch(es):** <feat|fix|chore/slug ...>
- **Período:** <primeiro turno> → <último turno>
- **Gerado em:** <YYYY-MM-DD HH:MM>
- **Fonte:** transcripts locais (`~/.claude/projects`) + artefatos SDD do repo
- **Custo:** ESTIMATIVA — preços em `sdd/report/pricing.json` (as_of <data>)

> Relatório de uso do SDD: esforço (tokens, tempo, custo) + qualidade/governança.
> Gerado por `sdd-report`. **Nada saiu da máquina** — só leu arquivos locais.

## Resumo executivo

<2–4 linhas: custo total estimado, tempo ativo, nº de tasks entregues, veredito do
acceptance, e o argumento — ex.: "X% do gasto foi em decisão (requirements+design),
empurrando o erro pra esquerda; execução saiu barata em Sonnet/Haiku".>

## Custo & esforço

| Métrica | Valor |
|---------|-------|
| Custo estimado | US$ <x> (~R$ <y>) |
| Tokens (in / out / thinking / cache-read / cache-write) | <...> |
| Tempo ativo / decorrido | <hh:mm> / <hh:mm> |
| Turnos / tool calls | <n> / <n> |
| Tasks entregues | <n> |
| Custo por task | US$ <x/n> |

### Por fase

| Fase | Modelo(s) | Turnos | Tokens | Custo est. |
|------|-----------|--------|--------|-----------|
| requirements | opus | <n> | <n> | US$ <x> |
| design | opus | | | |
| delivery | sonnet | | | |
| ... | | | | |

### Por modelo

| Modelo | Turnos | Tokens | Custo est. |
|--------|--------|--------|-----------|
| claude-opus-4-8 | <n> | <n> | US$ <x> |
| claude-sonnet-5 | | | |
| claude-haiku-4-5 | | | |

### Pensar vs executar (shift-left)

- **Decisão** (constitution, discovery, requirements, design, acceptance): **<X%>** do custo
- **Execução** (backlog, analyze, delivery) + **registro** (state): **<Y%>**
- Leitura: <o SDD investiu cedo, no texto, antes de gastar execução — ou o contrário, com o porquê>

## Qualidade & governança

| Indicador | Valor | Fonte |
|-----------|-------|-------|
| Tasks `done` com evidência objetiva | <n/N> | tasks.md |
| Inconsistências pegas pelo `sdd-analyze` (antes de codar) | <n> | state.md / analyze |
| Re-trabalho (tasks reabertas / `blocked`) | <n> | tasks.md |
| Checkpoints humanos (pedido + por task) | <n> | requirements.md / state.md |
| Guidelines aplicadas | <lista> | design.md |
| Conformidade com a CONSTITUTION | ok / ressalvas | acceptance.md |
| Veredito do acceptance | aprovado / ressalvas / reprovado | acceptance.md |

## Observações & limites

- **Custo é estimativa** (`sdd/report/pricing.json`) — edite se o preço ou o seu plano mudou.
- Atribuição por fase usa a **última skill `sdd-*` ativada** na sessão; turnos fora de skill
  aparecem como "(fora de skill)".
- **Cache-read é barato** (~0,1× input) e costuma dominar a contagem de tokens — por isso
  tokens brutos **não** são proporcionais ao custo.
- Tempo "ativo" ignora intervalos ociosos > 5 min entre turnos; "decorrido" é o intervalo total.

## Metodologia

- **Esforço:** `python3 ${CLAUDE_PLUGIN_ROOT}/sdd/report/usage.py --project-dir <raiz> [--branch <b>]`
- **Qualidade:** leitura de `specs/<NNN>/{requirements,tasks,acceptance}.md` e `state.md`
