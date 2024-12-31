#!/bin/bash

# Usage: ./source_chowdhurydsp.sh <project> <tag>
#        ./source_chowdhurydsp.sh ChowMultiTool v1.0.0

git clone https://github.com/Chowdhury-DSP/$1
cd $1
git checkout $é
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $é"
    exit 1
fi
git submodule update --init --recursive -progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
