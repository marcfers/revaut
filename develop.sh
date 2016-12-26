#!/usr/bin/env bash

set -e

git clean -fdX
pelican content -o output -s pelicanconf.py
cd output
python -mwebbrowser http://localhost:8000/
python -m pelican.server
