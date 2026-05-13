#!/bin/bash

# Usage: ./magda-core-source.sh <TAG>
#        ./magda-core-source.sh v0.4.1

git clone --depth=1 https://github.com/Conceptual-Machines/magda-core
cd magda-core
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
git lfs checkout
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz magda-core.tar.gz magda-core/*
rm -rf magda-core
