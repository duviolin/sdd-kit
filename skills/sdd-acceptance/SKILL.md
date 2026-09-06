---
name: sdd-acceptance
description: >-
  Use to validate a finished SDD delivery against the branch diff before merge.
  Auto-use when the user says "valida", "validate", "aceita", "pronto pra merge",
  or when the last task of a feature is done. Checks scope, coverage, evidence,
  tests and constitution conformance, then writes acceptance.md with the verdict.
---

# sdd-acceptance

Valida a entrega de `specs/<NNN>-<slug>/` contra o **diff da branch** e emite `acceptance.md`.

## Passos

1. Ler `constitution.md`, `requirements.md`, `design.md` e `tasks.md` do `<NNN>-<slug>`.
2. Obter o diff da branch de trabalho contra a base (ex.: `git diff <base>...HEAD --stat` e
   detalhado). Conferir que os arquivos tocados **batem com o design** e nada relevante ficou fora.
3. Para cada critério de aceite, confirmar cobertura por evidência real (teste verde, saída,
   comportamento) — incluindo os **caminhos de erro/borda**. Rodar/observar os testes da
   "Estratégia de testes" e da "Validação planejada" do design.
4. **Gate de qualidade medível:** rodar o comando de cobertura do projeto e confrontar com o piso
   da `constitution.md`. Confirmar: todo CA provado? todo caminho de erro coberto? NFR
   (perf/segurança/acessibilidade) com evidência objetiva? Escopo entregue = escopo dos requisitos?
   Nada fora do escopo no diff? A entrega respeitou a `constitution.md`?
5. Preencher `${CLAUDE_PLUGIN_ROOT}/sdd/templates/acceptance.md` e gravar `acceptance.md` com o **veredito**
   (`aprovado` / `aprovado-com-ressalvas` / `reprovado`).

## Regras

- Não emitir `aprovado` sem evidência objetiva de todos os critérios (senão `reprovado` ou ressalva).
- Violação de princípio da `constitution.md` é motivo de `reprovado` ou ressalva, conforme gravidade.
- Se reprovado, listar exatamente o que falta para reabrir — vira novas tasks.
- O `acceptance.md` é o registro auditável final da entrega; deve se sustentar sozinho,
  sem depender do histórico da conversa.

## Estado (lock)

- Respeitar o protocolo do `sdd-state`: ler `state.md` antes de agir; se **outra** feature estiver `in_progress`, parar e avisar. Ao iniciar/fechar esta etapa, atualizar o bloco LOCK e o histórico.
