#!/bin/bash

# Usage: ./nine-strip-source.sh <TAG>
#        ./nine-strip-source.sh v0.1.2

git clone https://github.com/blablack/nine-strip
cd nine-strip
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz nine-strip.tar.gz nine-strip/*
rm -rf nine-strip
