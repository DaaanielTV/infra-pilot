#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <version> [notes]" >&2
  exit 1
fi
VERSION="$1"
NOTES="${2:-Release ${VERSION}}"

echo "Creating release ${VERSION}..."

if git tag | grep -q "^v$VERSION$"; then
  echo "Tag v${VERSION} already exists" >&2
  exit 1
fi

echo "\n changelog: adding entry to CHANGELOG.md if present..."
if [ -f CHANGELOG.md ]; then
  echo -e "\n## ${VERSION}\n- ${NOTES}\n" >> CHANGELOG.md
  git add CHANGELOG.md
fi

git commit -m "docs(release): prepare release ${VERSION} - ${NOTES}"
git tag -a "v${VERSION}" -m "Release ${VERSION}: ${NOTES}"
echo "Release $VERSION prepared. You can push with: git push origin --tags" 
