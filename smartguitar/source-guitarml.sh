#!/bin/bash

# Usage: ./source-guitarml.sh <project> <tag>
#        ./source-guitarml.sh SmartGuitarAmp v1.3

git clone https://github.com/GuitarML/$1
cd $1
git checkout $2
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $2"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
