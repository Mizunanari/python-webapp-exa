#!/bin/bash

# 仮想環境を作らない
poetry config virtualenvs.create false

poetry install

printf '\n\033[1;37;44m%s\033[m\n' 'F5 または 実行とデバックからFastAPIを実行できます!'