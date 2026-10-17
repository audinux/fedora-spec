#!/bin/bash

# Usage: ./stagerig-source.sh <TAG>
#        ./stagerig-source.sh v0.1.41

git clone https://github.com/dguedry/stagerig/
cd stagerig
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
if [ $? -ne 0 ]; then
    echo "Problem with submodules"
    exit 1
fi
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz stagerig.tar.gz stagerig/*
rm -rf stagerig
md5sum stagerig.tar.gz > stagerig-md5sum.txt
