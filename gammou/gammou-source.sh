#!/bin/bash

# Usage: ./gammou-source.sh <TAG>
# ./gammou-source.sh master

git clone https://github.com/aliefhooghe/Gammou
cd Gammou
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Gammou.tar.gz Gammou/*
rm -rf Gammou
