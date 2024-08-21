#!/bin/bash

# Usage: ./gammou-source.sh <TAG>
# ./gammou-source.sh master

git clone https://github.com/aliefhooghe/Gammou
cd Gammou
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Gammou.tar.gz Gammou/*
rm -rf Gammou
