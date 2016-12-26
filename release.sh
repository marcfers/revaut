#!/usr/bin/env bash

set -e

git clean -fdX
pelican content -o output -s publishconf.py
ghp-import output
git push origin gh-pages
