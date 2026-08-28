#!/bin/sh
set -eu

usage() {
  echo "Usage: ./scripts/install.sh [--force] /path/to/fabric-custom-patterns" >&2
  echo "Set RISKSTITCH_FABRIC_PATTERNS_DIR instead of passing a path if preferred." >&2
}

force=0
if [ "${1:-}" = "--force" ]; then
  force=1
  shift
fi

target="${1:-${RISKSTITCH_FABRIC_PATTERNS_DIR:-}}"
if [ -z "$target" ]; then
  usage
  exit 2
fi

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_dir=$(CDPATH= cd -- "$script_dir/.." && pwd)
target_abs=$(python3 -c 'import os,sys; print(os.path.abspath(sys.argv[1]))' "$target")

if [ "$target_abs" = "/" ] || [ "$target_abs" = "$HOME" ] || [ "$target_abs" = "$repo_dir" ]; then
  echo "Refusing unsafe target: $target_abs" >&2
  exit 2
fi

mkdir -p "$target_abs"

installed=0
skipped=0
for source_dir in "$repo_dir"/patterns/grc_*; do
  pattern=$(basename "$source_dir")
  destination="$target_abs/$pattern"
  if [ -e "$destination" ] && [ "$force" -ne 1 ]; then
    echo "skip $pattern (already exists; use --force to replace system.md)"
    skipped=$((skipped + 1))
    continue
  fi
  mkdir -p "$destination"
  cp "$source_dir/system.md" "$destination/system.md"
  echo "install $pattern"
  installed=$((installed + 1))
done

echo "Installed: $installed; skipped: $skipped; target: $target_abs"
