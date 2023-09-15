#!/bin/bash

# ./rerdavies-source.sh <project> <tag>
# ./rerdavies-source.sh ToobAmp v1.0.29

git clone https://github.com/rerdavies/$1
cd $1
git checkout $2
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
