# sdd-kit — fluxo SDD portátil para o Claude Code

Conjunto de **9 skills** (`sdd-*`) + **templates** + **guidelines** + **hook de trava** que
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
├── skills/                 # as 9 skills sdd-* (viram /sdd-kit:sdd-*)
│   └── sdd-{constitution,discovery,requirements,design,backlog,analyze,delivery,acceptance,state}/SKILL.md
├── hooks/
│   └── hooks.json          # registra a trava PreToolUse (sdd-lock)
├── sdd/                    # assets referenciados via ${CLAUDE_PLUGIN_ROOT}/sdd
│   ├── templates/          # CONSTITUTION ARCHITECTURE STATE requirements design tasks acceptance
│   ├── guidelines/         # tdd test-strategy solid defensive-programming rich-domain dry kiss
│   │                       # yagni clean-code error-handling secure-by-default code-review
│   └── hooks/              # sdd-lock.py — o script da trava
├── docs/index.html         # documentação visual
└── install.sh              # helper de teste local + validação
```

## Fluxo

```
sdd-constitution → sdd-discovery → sdd-requirements → [APROVAÇÃO HUMANA] → sdd-design → sdd-backlog → sdd-analyze → sdd-delivery → sdd-acceptance
```

`sdd-state` é transversal: mantém `state.md` (o que está rodando, onde paramos) e `.sdd/lock`
(uma feature ativa por vez). O hook `sdd-lock` reforça a trava bloqueando escrita fora da branch dona.

Cada feature gera uma trilha versionada em `specs/<NNN>-<slug>/` no projeto-alvo.
