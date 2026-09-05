# STATE — <projeto>

- **Atualizado:** <YYYY-MM-DD HH:MM>

> Fonte única de "o que está em execução". Toda skill lê este arquivo **antes de agir** e o
> atualiza ao entrar/sair de uma etapa. A trava é reforçada pelo hook `sdd-lock` (PreToolUse) +
> arquivo `.sdd/lock`. É isto que evita duas janelas se sobrescreverem e diz onde retomar.

## Em execução (LOCK)

- **Feature:**    <NNN-slug | nenhuma>
- **Etapa:**      <sdd-requirements | sdd-design | sdd-backlog | sdd-analyze | sdd-delivery | sdd-acceptance | —>
- **Branch:**     <feat|fix|chore/slug | —>
- **Status:**     free            # free | in_progress | paused | blocked
- **Dono:**       <você / marca da sessão>
- **Task atual:** <Tn de N | —>
- **Início:**     <YYYY-MM-DD HH:MM | —>
- **Atualizado:** <YYYY-MM-DD HH:MM | —>

## Histórico

| Quando             | Feature   | Etapa            | Evento                                        |
|--------------------|-----------|------------------|-----------------------------------------------|
| <YYYY-MM-DD HH:MM> | <NNN-slug> | <etapa>         | iniciado / aprovado / pausado / bloqueado / concluído / liberado |
