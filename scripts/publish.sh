#!/usr/bin/env sh

set -xe

main() {
    python3 -m pip install setuptools wheel twine
    python3 setup.py sdist bdist_wheel
    python3 -m twine upload dist/*
}

main "$@"
