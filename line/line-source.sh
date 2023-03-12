#!/bin/bash

# Usage: ./line-source.sh <TAG>
# ./line-source.sh v0.4.19

git clone https://github.com/pd3v/line
cd line
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz line.tar.gz line/*
rm -rf line
