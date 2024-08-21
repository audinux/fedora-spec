#!/bin/bash

# Usage:
# ./source-prom <TAG>
# ./source-prom master

git clone https://github.com/DISTRHO/ProM
cd ProM
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ProM.tar.gz ProM/*
rm -rf ProM
