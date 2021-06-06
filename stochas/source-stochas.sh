#!/bin/bash

# Usage: ./source-stochas.sh <tag>
#        ./source-stochas.sh v1.3.5

git clone https://github.com/surge-synthesizer/stochas
cd stochas
# git checkout origin/release/$1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz stochas.tar.gz stochas/*
rm -rf stochas
