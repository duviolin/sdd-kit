#!/usr/bin/env bash
# sdd-kit — instalação via plugin do Claude Code.
#
# Este pacote é um PLUGIN + MARKETPLACE do Claude Code. A instalação de verdade é feita
# de dentro do Claude Code, com /plugin — não copiando arquivos para ~/.claude (as skills
# usam ${CLAUDE_PLUGIN_ROOT}, que só resolve quando carregadas como plugin).
#
# Este script só ajuda no teste local durante o desenvolvimento.
set -euo pipefail
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cat <<EOF
sdd-kit — Spec-Driven Development portátil (plugin do Claude Code)

INSTALAR (recomendado) — de dentro do Claude Code:

  /plugin marketplace add duviolin/sdd-kit
  /plugin install sdd-kit@sdd-kit

  Abra uma sessão nova. As skills viram /sdd-kit:sdd-requirements etc. e disparam
  também por linguagem natural. A trava (hook sdd-lock) é ativada pelo próprio plugin.

TESTAR LOCALMENTE (sem instalar) — a partir deste diretório:

  claude --plugin-dir "$SRC"

VALIDAR o pacote antes de publicar:

  claude plugin validate "$SRC"
EOF

if command -v claude >/dev/null 2>&1; then
  echo
  echo "→ Validando este pacote..."
  claude plugin validate "$SRC" || true
fi
