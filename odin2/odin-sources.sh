#!/bin/bash

# Usage: ./odin-source.sh <TAG>
# ./odin-source.sh v2.3.1

git clone https://github.com/TheWaveWarden/odin2
cd odin2
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz odin2.tar.gz odin2/*
rm -rf odin2
