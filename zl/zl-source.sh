#!/bin/bash

# ./zl-source.sh <project> <tag>
# ./zl-source.sh ZLEqualizer 0.2.2

git clone https://github.com/ZL-Audio/$1
cd $1
git checkout $2
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
