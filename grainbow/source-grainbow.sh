#!/bin/bash

# Usage: ./source-grainbow.sh <tag>
#        ./source-grainbow.sh v0.4.0

git clone https://github.com/bboettcher3/gRainbow
cd gRainbow
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz gRainbow.tar.gz gRainbow/*
rm -rf gRainbow
