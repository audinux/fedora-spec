#!/bin/bash

VERSION="$1"

git clone https://github.com/sadko4u/lsp-plugins
cd lsp-plugins
git checkout $VERSION
git submodule init
git submodule update

make fetch
make config

find . -name .git --exec rm -rf {} \;
cd ..
tar cvfz lsp-plugins.tar.gz lsp-plugins/*
rm -rf lsp-plugins
