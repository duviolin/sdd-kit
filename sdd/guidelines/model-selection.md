# Model Selection — qual modelo do Claude usar em cada fase

Cada fase do SDD tem uma demanda diferente: umas exigem **julgamento e raciocínio**
(decidir escopo, arquitetura, aprovar entrega), outras são **estruturadas e mecânicas**
(quebrar tarefas, anotar estado). Escolher o modelo por fase economiza custo sem perder
qualidade onde ela importa.

Regra de bolso:

- **Opus** *pensa* — decisões de alto impacto e difíceis de reverter.
- **Sonnet** *executa* — trabalho estruturado com bom custo-benefício.
- **Haiku** *anota* — tarefas triviais, rápidas e baratas.

## Benefícios

- **Gasta onde importa**: o modelo mais forte fica nas fases de decisão (onde um erro se propaga em
  cascata); as mecânicas rodam num modelo mais barato. Qualidade onde decide, economia onde executa.
- **Zero fricção**: a troca é automática por fase — ninguém precisa lembrar de ajustar o `/model`.
- **Seguro por padrão**: sem acesso ao modelo, mantém o atual (não quebra); o override dura o turno e
  reverte (não sequestra a sessão).
- **Ajustável**: continua sendo um ponto de partida — `/model` sobrepõe pontualmente, `inherit`/remover
  desliga.

## Sugestão por fase

| Fase | Modelo | Por quê |
|------|--------|---------|
| `sdd-constitution` | **Opus** | Define princípios que valem pra tudo; um erro aqui se propaga em cascata. Roda raramente. |
| `sdd-discovery` | **Opus** (repo grande/desconhecido) · **Sonnet** (repo pequeno/familiar) | Ler muito código e sintetizar a arquitetura pede contexto amplo e raciocínio. |
| `sdd-requirements` | **Opus** | Traduzir história → spec, resolver ambiguidade e fechar escopo é a fase de maior julgamento. |
| `sdd-design` | **Opus** | Decisões técnicas e trade-offs de arquitetura — o núcleo pensante do fluxo. |
| `sdd-backlog` | **Sonnet** | Quebrar um design aprovado em tarefas é estruturado; Sonnet resolve com custo menor. |
| `sdd-analyze` | **Sonnet** | Gate barato de consistência entre artefatos; não escreve código. |
| `sdd-delivery` | **Sonnet** (padrão) · **Opus** (task espinhosa) | Implementar task a task; suba pra Opus só nas tarefas difíceis. |
| `sdd-acceptance` | **Opus** | Validação adversarial contra o diff antes do merge — vale o modelo mais criterioso. |
| `sdd-state` | **Haiku** | Bookkeeping de `state.md` e do lock; tarefa trivial e frequente. |

## Troca automática (já embutida)

Cada `SKILL.md` declara o modelo da fase no frontmatter (`model:`). Quando a skill dispara, o
Claude Code **troca sozinho** pro modelo indicado **pelo resto daquele turno** e volta pro modelo
da sessão no próximo prompt. Você não precisa mexer no `/model` — o kit pilota.

Como isso se comporta:

- **Degrada com segurança**: se o seu plano/organização não libera o modelo (ex.: sem Opus), a
  sessão **mantém o modelo atual** em vez de falhar. Nada quebra.
- **Não gruda**: o override dura o turno e reverte. Em `sdd-delivery` (uma task por turno) reaplica
  a cada disparo — que é o comportamento desejado.
- **Não pergunta**: a troca é silenciosa a cada turno em que a skill roda. Você "consente" ao manter
  o campo `model:`; não existe um "perguntar antes" nativo.

Overrides manuais quando quiser fugir do default:

- `/model` (ou o seletor do app) antes de disparar a skill sobrepõe pontualmente.
- `sdd-discovery`: em repo grande/desconhecido vale Opus; em repo pequeno/familiar, Sonnet basta.
- `sdd-delivery`: se o Sonnet está patinando numa task difícil, suba pra Opus só naquela task.

Para **desligar** a troca automática de uma fase: troque o valor de `model:` para `inherit`
(mantém o modelo da sessão) ou remova a linha do frontmatter daquela skill.

## Anti-padrões

- Usar Opus pra `sdd-state` (anotar onde parou) — custo alto pra ganho nenhum.
- Usar Haiku pra `sdd-design` ou `sdd-requirements` — economia que sai cara em retrabalho.
- Trocar de modelo no meio de uma task e perder o contexto do que já foi decidido.

## Aplicação no SDD

- Trate esta guideline como referência: consulte-a ao iniciar cada fase, não como regra travada.
- A qualidade das fases de decisão (Opus) sustenta o custo baixo das fases de execução —
  um bom `requirements`/`design` deixa `backlog` e `delivery` mais mecânicos e baratos.
