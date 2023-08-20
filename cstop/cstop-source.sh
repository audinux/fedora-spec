#!/bin/bash

# Usage: ./cstop-source.sh <tag>
#        ./cstop-source.sh v1.0.0

git clone https://github.com/calgoheen/cStop
cd cStop
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz cStop.tar.gz cStop/*
rm -rf cStop
