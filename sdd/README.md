# SDD — fluxo portátil (skills `sdd-*`)

Spec-Driven Development como um conjunto de skills globais do Claude Code. Roda em
**qualquer projeto**, sem copiar nada por repo. Toda a trilha fica versionada no
próprio repositório-alvo (auditoria persistida), independente do histórico da conversa.

## Ordem do fluxo

```
sdd-constitution        (opcional, 1x por projeto — princípios inegociáveis)
sdd-discovery           (opcional, 1x por projeto / quando muda de forma relevante)
        │
        ▼
sdd-requirements ─► [APROVAÇÃO HUMANA] ─► sdd-design ─► sdd-backlog ─► sdd-analyze ─► sdd-delivery ─► sdd-acceptance
```

- **sdd-constitution** → `CONSTITUTION.md` (princípios inegociáveis, nível projeto).
- **sdd-discovery** → `ARCHITECTURE.md` (nível projeto, evolutivo).
- **sdd-requirements** → `specs/<NNN>-<slug>/requirements.md` (EARS). **Para e pede aprovação. Não avança sozinha.**
- **sdd-design** → `specs/<NNN>-<slug>/design.md` (só depois dos requisitos aprovados).
- **sdd-backlog** → `specs/<NNN>-<slug>/tasks.md`.
- **sdd-analyze** → gate de consistência (requirements ↔ design ↔ tasks). Não escreve artefato; bloqueia se algo não bater.
- **sdd-delivery** → executa **uma task por vez**, só fecha com **evidência objetiva** (red-first).
- **sdd-acceptance** → valida a entrega contra o diff da branch → `specs/<NNN>-<slug>/acceptance.md`.
- **sdd-state** (transversal) → mantém `STATE.md` + `.sdd/lock`: uma feature ativa por vez, retomada segura.

## Convenção de artefatos (no projeto-alvo)

```
<projeto>/
├── CONSTITUTION.md                 # princípios inegociáveis (único por projeto)
├── ARCHITECTURE.md                 # visão técnica real (único por projeto)
├── STATE.md                        # o que está rodando + histórico (sdd-state)
├── .sdd/lock                       # trava (feature/branch/dono/ts) — reforçada pelo hook
└── specs/
    └── <NNN>-<slug>/
        ├── requirements.md
        ├── design.md
        ├── tasks.md
        └── acceptance.md
```

- `<NNN>` = próximo número livre (varra `specs/`, pegue o maior + 1, 3 dígitos: `001`, `002`…).
- `<slug>` = kebab-case curto do título da feature.
- Cada artefato tem um cabeçalho `Status:` — o estado vive no arquivo, não numa conversa.

## Gates de aprovação

- **requirements → design**: exige um "aprovado"/"segue" humano explícito. A skill
  `sdd-requirements` **nunca** gera o design no mesmo turno.
- **backlog → delivery**: `sdd-analyze` precisa dar **consistente** antes de codar.
- **última task → acceptance**: `sdd-acceptance` só emite `acceptance.md: aprovado` com evidência —
  cobertura conferida contra o piso da `CONSTITUTION.md`, todo CA e caminho de erro provado.

## Trava de execução (STATE.md + hook)

- `STATE.md` (raiz) é a fonte única de "o que está rodando / onde paramos"; `.sdd/lock` guarda a
  trava (feature, branch, dono, timestamp). Gerenciados por `sdd-state`.
- O script `sdd/hooks/sdd-lock.py` (PreToolUse) **bloqueia Edit/Write** quando o lock pertence a
  outra branch — evita duas janelas se sobrescreverem. É **advisory reforçada**, não mutex de SO:
  edições a `STATE.md`/`.sdd` seguem liberadas, e lock > 8h é tratado como expirado.
- **Registro automático:** o plugin declara o hook em `hooks/hooks.json`; ele passa a valer assim
  que o plugin é instalado/ativado — sem editar `settings.json` na mão:

  ```json
  { "hooks": { "PreToolUse": [
    { "matcher": "Edit|Write|MultiEdit|NotebookEdit",
      "hooks": [ { "type": "command", "command": "python3 \"${CLAUDE_PLUGIN_ROOT}/sdd/hooks/sdd-lock.py\"" } ] }
  ] } }
  ```

## Assets deste pacote

- `templates/` — esqueleto de cada artefato. As skills copiam daqui e preenchem.
- `guidelines/` — princípios de engenharia citados por `sdd-design` e `sdd-delivery`
  (`tdd`, `test-strategy`, `solid`, `defensive-programming`, `rich-domain`, `dry`, `kiss`, `yagni`,
  `clean-code`, `error-handling`, `secure-by-default`, `code-review`).
- `hooks/` — `sdd-lock.py`, a trava PreToolUse.

> As skills referenciam estes assets via `${CLAUDE_PLUGIN_ROOT}/sdd/...`, resolvido pelo Claude Code
> quando o plugin está ativo. Se `sdd/` estiver ausente/parcial, reinstale o plugin.
