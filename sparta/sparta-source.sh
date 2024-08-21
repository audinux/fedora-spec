#!/bin/bash

# Usage: ./sparta-sources.sh <TAG>
#        ./sparta-sources.sh v1.14.1

git clone  https://github.com/leomccormack/SPARTA
cd SPARTA
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz SPARTA.tar.gz SPARTA/*
rm -rf SPARTA
