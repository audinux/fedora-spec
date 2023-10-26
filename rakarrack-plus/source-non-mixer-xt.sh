#!/bin/bash

# Usage: ./source-non-mixer-xt.sh <tag>
#        ./source-non-mixer-xt.sh 1.0.5

git clone https://github.com/Stazed/non-mixer-xt
cd non-mixer-xt
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz non-mixer-xt.tar.gz non-mixer-xt/*
rm -rf non-mixer-xt
