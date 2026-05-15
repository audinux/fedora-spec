#!/bin/bash

# Usage: ./protoplug-sources.sh <TAG>
#        ./protoplug-sources.sh fixes

git clone https://github.com/ycollet/protoplug/
cd protoplug
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz protoplug.tar.gz protoplug/*
rm -rf protoplug
