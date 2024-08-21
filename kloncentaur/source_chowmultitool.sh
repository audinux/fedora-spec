#!/bin/bash

# Usage: ./source_chowmultitool.sh <tag>
#        ./source_chowmultitool.sh v1.0.0

git clone --recursive https://github.com/Chowdhury-DSP/ChowMultiTool
cd ChowMultiTool
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive -progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ChowMultiTool.tar.gz ChowMultiTool/*
rm -rf ChowMultiTool
