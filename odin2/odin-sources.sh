#!/bin/bash

# Usage: ./odin-sources.sh <TAG>
# ./odin-sources.sh v2.3.4

git clone https://github.com/TheWaveWarden/odin2
cd odin2
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz odin2.tar.gz odin2/*
rm -rf odin2
