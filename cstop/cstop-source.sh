#!/bin/bash

# Usage: ./cstop-source.sh <tag>
#        ./cstop-source.sh v1.0.0

git clone https://github.com/calgoheen/cStop
cd cStop
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz cStop.tar.gz cStop/*
rm -rf cStop
