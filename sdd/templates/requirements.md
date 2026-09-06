# REQUIREMENTS — <título da feature>

- **ID:** <NNN>-<slug>
- **Status:** draft | awaiting_approval | approved | superseded
- **Origem:** <ticket / história / conversa / código / bug — link ou referência>
- **Autor:** <quem>
- **Data:** <YYYY-MM-DD>

## Problema / motivação

<Qual dor ou necessidade. O que muda para quem usa. Por que agora.>

## Escopo

**Dentro:**
- <...>

**Fora (explicitamente):**
- <...>

## Requisitos (notação EARS)

Escreva cada requisito num dos padrões EARS — remove ambiguidade e vira teste direto:

- **Ubíquo:** THE SYSTEM SHALL <comportamento sempre válido>.
- **Evento:** WHEN <gatilho>, THE SYSTEM SHALL <comportamento>.
- **Estado:** WHILE <estado>, THE SYSTEM SHALL <comportamento>.
- **Opcional:** WHERE <feature/config presente>, THE SYSTEM SHALL <comportamento>.
- **Indesejado:** IF <condição de erro>, THEN THE SYSTEM SHALL <resposta>.

- **R1** — WHEN <...>, THE SYSTEM SHALL <...>.
- **R2** — IF <...>, THEN THE SYSTEM SHALL <...>.
- **RN1** — THE SYSTEM SHALL <requisito não-funcional: performance, segurança, acessibilidade...>.

## Critérios de aceite

- **CA1** — Dado <contexto>, quando <ação>, então <resultado observável>.
- **CA2** — <...>

> Cada CA deve ser verificável por teste ou evidência objetiva. Rastreie CA ↔ requisito.

## Premissas

- <O que assumimos como verdadeiro para caber no escopo.>

## Dúvidas em aberto

- [ ] <pergunta que precisa de decisão humana antes/durante o design>

## Rastreabilidade

| Requisito | Critério(s) | Task(s) | Evidência |
|-----------|-------------|---------|-----------|
| R1        | CA1         | (tasks) | (delivery) |

## Checklist de qualidade (antes de pedir aprovação)

- [ ] Requisitos escritos em EARS, sem ambiguidade.
- [ ] Todo critério de aceite é **verificável** (vira teste/evidência objetiva).
- [ ] Cada requisito tem ao menos um critério de aceite mapeado.
- [ ] Escopo "fora" preenchido explicitamente (anti scope-creep).
- [ ] Sem detalhe de implementação (o "como" é do design, não daqui).
- [ ] Nada contraria a `constitution.md` do projeto.
- [ ] Dúvidas críticas viraram pergunta em aberto, não achismo.

---
**Gate:** este documento não avança para o design sem aprovação humana explícita.
