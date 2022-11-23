#!/bin/bash

# Usage: ./source-guitarml.sh <project> <tag>
#        ./source-guitarml.sh SmartGuitarAmp v1.3

git clone https://github.com/GuitarML/$1
cd $1
git checkout origin/release/$2
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
