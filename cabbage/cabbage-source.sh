#!/bin/bash

# Usage: ./cabbage-sources.sh <TAG>
# ./cabbage-sources.sh v2.9.0

git clone https://github.com/rorywalsh/cabbage
cd cabbage
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
# Cleanup macos things
rm -rf Csound CLIConverter *.dmg *.dylib
cd ..
tar cvfz cabbage.tar.gz cabbage/*
rm -rf cabbage
