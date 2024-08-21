#!/bin/bash

# Usage: ./source-grainbow.sh <tag>
#        ./source-grainbow.sh v0.4.0

git clone https://github.com/bboettcher3/gRainbow
cd gRainbow
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz gRainbow.tar.gz gRainbow/*
rm -rf gRainbow
