#!/bin/bash

# Usage: ./source-stochas.sh <tag>
#        ./source-stochas.sh v1.3.9

git clone https://github.com/surge-synthesizer/stochas
cd stochas
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz stochas.tar.gz stochas/*
rm -rf stochas
