#!/bin/bash

# ./brummer10-source.sh <project> <tag>
# ./brummer10-source.sh xtuner v1.0

git clone https://github.com/brummer10/$1
cd $1
git checkout $2
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
