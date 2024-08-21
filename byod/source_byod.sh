#!/bin/bash

# Usage: ./source_byod.sh <tag>
#        ./source_byod.sh v1.0.1

git clone https://github.com/Chowdhury-DSP/BYOD
cd BYOD
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz BYOD.tar.gz BYOD/*
rm -rf BYOD
