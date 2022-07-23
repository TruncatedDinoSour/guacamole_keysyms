#!/usr/bin/env sh

set -xe

main() {
    python3 pip install setuptools wheel twine
    python3 setup.py sdist bdist_wheel
    python3 -m twine upload dist/*
}

main "$@"
