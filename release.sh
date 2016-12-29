#!/usr/bin/env bash

source virtualenvwrapper.sh
workon workspacePelican

git clean -fdX
pelican content -o revaut -s publishconf.py
ghp-import revaut
git push origin gh-pages
