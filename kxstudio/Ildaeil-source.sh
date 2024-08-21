#!/bin/bash

# Usage: ./Ildaeil-source.sh <tag>
#        ./Ildaeil-source.sh v1.2

git clone https://github.com/DISTRHO/Ildaeil
cd Ildaeil
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Ildaeil.tar.gz Ildaeil/*
rm -rf Ildaeil
