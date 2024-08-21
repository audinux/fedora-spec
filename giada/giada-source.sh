#!/bin/bash

# Usage: ./giada-source.sh <TAG>
#        ./giada-source.sh v1.0.0

git clone https://github.com/monocasual/giada
cd giada
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz giada.tar.gz giada/*
rm -rf giada
