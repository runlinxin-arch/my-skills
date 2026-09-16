#!/usr/bin/env bash
# Create the skill's virtualenv and install the conversion dependencies.
# Run once: bash scripts/setup.sh
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="$SKILL_DIR/.venv"
PYTHON="${PYTHON:-python3}"

if [ ! -d "$VENV" ]; then
  echo "Creating virtualenv at $VENV"
  "$PYTHON" -m venv "$VENV"
fi

"$VENV/bin/python" -m pip install --upgrade pip
"$VENV/bin/python" -m pip install -r "$SKILL_DIR/requirements.txt"

echo
echo "Done. Convert with:"
echo "  $VENV/bin/python $SKILL_DIR/scripts/convert.py <file> [more files...]"
