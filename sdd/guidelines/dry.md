# DRY — Don't Repeat Yourself

Cada pedaço de conhecimento tem uma única representação canônica no sistema.

## Regras práticas

- Duplicação de **conhecimento** (regra, fórmula, constante) é dívida — centralize.
- Duplicação **acidental** (dois trechos parecidos por coincidência) pode ficar: só una quando
  as duas realmente mudam pelo mesmo motivo.
- Regra de negócio, validação e mágica-de-string moram num lugar só.

## Anti-padrões

- Abstração prematura: extrair "helper" antes de ter 2–3 usos reais e um motivo comum de mudança.
- Copiar-colar lógica de negócio entre camadas.
- Constante repetida (mesmo timeout/limite espalhado em vários arquivos).

## Aplicação no SDD

- `sdd-design`: aponte onde o conhecimento deve viver (uma fonte da verdade).
- `sdd-delivery`: no passo de refactor do TDD, una duplicação real; equilibre com `yagni`.
