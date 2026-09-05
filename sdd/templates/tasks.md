# TASKS — <título da feature>

- **ID:** <NNN>-<slug>
- **Design:** ./design.md
- **Data:** <YYYY-MM-DD>

> Uma task por unidade executável e verificável. `sdd-delivery` faz uma por vez e só marca
> `done` com evidência objetiva colada abaixo. Marque `[P]` no título das tasks que podem
> rodar em paralelo (sem dependência entre si).

## T1 — <título curto e acionável>

- **Status:** todo | in_progress | done | blocked
- **Origem:** <passo do design / requisito (R1, CA1)>
- **Fazer:** <o que exatamente>
- **Casos de borda/erro:** <inválido, vazio, duplicado, limite, dependência fora... (ver test-strategy)>
- **Evidência esperada:** <testes do caso feliz + dos casos de borda/erro verdes / saída / diff>
- **Bloqueios:** <nenhum | depende de T?>
- **Evidência obtida:** <preenchido pelo delivery — comando + resultado>

## T2 — <...> `[P]`

- **Status:** todo
- **Origem:** <...>
- **Fazer:** <...>
- **Evidência esperada:** <...>
- **Bloqueios:** <...>
- **Evidência obtida:** <...>

---
### Resumo

| Task | Status | Critérios cobertos | Paralela |
|------|--------|--------------------|----------|
| T1   | todo   | CA1 | não |
| T2   | todo   | CA2 | `[P]` |
