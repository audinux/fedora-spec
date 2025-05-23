#!/bin/bash

# Usage: ./fire-sources.sh <TAG>
# ./fire-sources.sh v0.9.8

git clone https://github.com/jerryuhoo/Fire/
cd Fire
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Fire.tar.gz Fire/*
rm -rf Fire
