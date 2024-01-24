#!/bin/bash

# ./wstd-source.sh <project> <tag>
# ./wstd-source.sh wstd-eq v1.0

git clone https://github.com/Wasted-Audio/$1
cd $1
git checkout $2
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
