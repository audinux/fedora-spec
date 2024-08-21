#!/bin/bash

# Usage: ./vocoder-sources.sh <TAG>
# ./vocoder-sources.sh main

git clone https://github.com/Stazed/vocoder
cd vocoder
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz vocoder.tar.gz vocoder/*
rm -rf vocoder
