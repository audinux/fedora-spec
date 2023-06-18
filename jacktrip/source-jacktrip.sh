#!/bin/bash

# Usage: ./source-jacktrip.sh <tag>
#        ./source-jacktrip.sh v1.10.0

git clone https://github.com/jacktrip/jacktrip
cd jacktrip
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz jacktrip.tar.gz jacktrip/*
rm -rf jacktrip
