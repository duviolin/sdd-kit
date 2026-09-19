# sdd-kit — fluxo SDD portátil para o Claude Code

Conjunto de **10 skills** (`sdd-*`) + **templates** + **guidelines** + **hook de trava** que
padronizam Spec-Driven Development em **qualquer projeto**, com auditoria persistida no próprio repo.

Documentação visual: **[docs/index.html](docs/index.html)** (abra no navegador).

## Instalar (plugin do Claude Code)

Este pacote é um **plugin + marketplace** do Claude Code. Cole os **dois comandos** abaixo
**dentro de uma sessão do Claude Code** (o terminal interativo do `claude`) — não no terminal
comum do sistema:

```
/plugin marketplace add duviolin/sdd-kit
/plugin install sdd-kit@sdd-kit
```

Depois **abra uma sessão nova**. As skills ficam disponíveis como `/sdd-kit:sdd-requirements`
(e disparam por linguagem natural); a trava (hook `sdd-lock`) é ativada pelo próprio plugin — sem
mexer em `~/.claude` na mão. O `/plugin` sozinho só abre o gerenciador; quem instala é o
`/plugin install` acima.

**Pré-requisitos:** Claude Code numa versão recente (com suporte a plugins) · rodar os comandos
dentro dele · **Python 3** na máquina só para a trava `sdd-lock` (sem ele, as skills funcionam;
só a trava fica inativa).

**Testar localmente** (sem instalar), a partir do clone:

```bash
claude --plugin-dir .
# ou: bash install.sh   (imprime as instruções + valida o pacote)
```

## Layout

```
sdd-kit/
├── .claude-plugin/
│   ├── plugin.json         # manifesto do plugin
│   └── marketplace.json    # manifesto do marketplace (source ".")
├── skills/                 # as 10 skills sdd-* (viram /sdd-kit:sdd-*)
│   └── sdd-{constitution,discovery,requirements,design,backlog,analyze,delivery,acceptance,state,report}/SKILL.md
├── hooks/
│   └── hooks.json          # registra a trava PreToolUse (sdd-lock)
├── sdd/                    # assets referenciados via ${CLAUDE_PLUGIN_ROOT}/sdd
│   ├── templates/          # CONSTITUTION ARCHITECTURE STATE requirements design tasks acceptance report
│   ├── guidelines/         # tdd test-strategy solid defensive-programming rich-domain dry kiss
│   │                       # yagni clean-code error-handling secure-by-default code-review
│   │                       # model-selection (qual modelo do Claude usar em cada fase)
│   ├── report/             # usage.py (agregador de tokens/tempo/custo) + pricing.json (editável)
│   └── hooks/              # sdd-lock.py — o script da trava
├── docs/index.html         # documentação visual
└── install.sh              # helper de teste local + validação
```

## Fluxo

```
sdd-constitution → sdd-discovery → sdd-requirements → [APROVAÇÃO HUMANA] → sdd-design → sdd-backlog → sdd-analyze → sdd-delivery ⟳ → sdd-acceptance
                                                                                                        (⟳ 1 task → prova → seu ok → próxima)
```

Você aprova em **dois momentos**: no pedido (`sdd-requirements` sempre para e espera o "aprovado")
e **a cada task** — `sdd-delivery` fecha uma task com a prova, para, e só segue pra próxima com o seu
ok. Assim o desvio aparece cedo, não no fim.

`sdd-state` é transversal: mantém `state.md` (o que está rodando, onde paramos) e `.sdd/lock`
(uma feature ativa por vez). O hook `sdd-lock` reforça a trava bloqueando escrita fora da branch dona.

## Modelo por fase (troca automática)

Cada skill declara no frontmatter (`model:`) o modelo do Claude indicado pra fase — **Opus** pensa
(constitution, discovery, requirements, design, acceptance), **Sonnet** executa (backlog, analyze,
delivery) e **Haiku** anota (state). O Claude Code troca sozinho ao disparar a skill e reverte no
próximo prompt. Não há cadeia de fallback: se você não tiver o modelo, ele **mantém o da sessão**
(não quebra) — por isso rode a sessão no melhor modelo que você tem, que o fallback já fica bom. O
racional completo, a estratégia de fallback e como desligar/ajustar estão em `sdd/guidelines/model-selection.md`.

## Métricas & relatório (`sdd-report`)

Depois de usar o SDD, `sdd-report` gera um `report.md` pra **justificar/analisar o uso** — juntando
duas fontes **locais** (nada sai da máquina):

- **Esforço** (dos transcripts do Claude Code): tokens, tempo, turnos, **mix de modelos** e **custo
  estimado**, atribuídos por **feature** (branch) e por **fase** (a skill `sdd-*` ativa).
- **Qualidade & governança** (dos artefatos SDD): cobertura de evidência, defeitos pegos pelo
  `analyze` antes de codar, re-trabalho, checkpoints humanos e o veredito do `acceptance`.

Rode com "relatório", "métricas", "quanto custou". O custo é **estimativa** via
`sdd/report/pricing.json` (editável). O agregador é determinístico:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/sdd/report/usage.py --project-dir . [--branch feat/<slug>]
```

Cada feature gera uma trilha versionada em `specs/<NNN>-<slug>/` no projeto-alvo.
