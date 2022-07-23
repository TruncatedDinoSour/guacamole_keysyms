#!/usr/bin/env sh

set -e

main() {
    git diff >/tmp/guacamole_keysyms.diff

    git add -A
    git commit -sa
    git push -u origin "$(git rev-parse --abbrev-ref HEAD)"
}

main "$@"
