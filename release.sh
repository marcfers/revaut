#!/usr/bin/env bash

source virtualenvwrapper.sh
workon workspacePelican

git clean -fdX
pelican content -o output -s publishconf.py
ghp-import output
git push origin gh-pages
