#!/usr/bin/env bash

source virtualenvwrapper.sh
workon workspacePelican

git clean -fdX
pelican content -o revaut -s pelicanconf.py
python -mwebbrowser http://localhost:8000/revaut
python -m pelican.server
