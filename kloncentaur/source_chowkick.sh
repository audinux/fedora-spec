#!/bin/bash

# Usage: ./source_chowkick.sh <tag>
#        ./source_chowkick.sh 1.2.0

git clone https://github.com/Chowdhury-DSP/ChowKick
cd ChowKick
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ChowKick.tar.gz ChowKick/*
rm -rf ChowKick
