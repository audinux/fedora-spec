#!/bin/bash

# Usage: ./source-houston4444.sh <project> <tag>
#        ./source-houston4444.sh RaySession v0.13.0

git clone https://github.com/Houston4444/$1
cd $1
git checkout $2
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
