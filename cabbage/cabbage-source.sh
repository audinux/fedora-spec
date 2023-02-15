#!/bin/bash

# Usage: ./cabbage-sources.sh <TAG>
# ./cabbage-sources.sh v2.9.0

git clone https://github.com/rorywalsh/cabbage
cd cabbage
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
# Cleanup macos things
rm -rf Csound CLIConverter *.dmg *.dylib
cd ..
tar cvfz cabbage.tar.gz cabbage/*
rm -rf cabbage
