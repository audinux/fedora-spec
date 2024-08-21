#!/bin/bash

# Usage: ./projectm-source.sh <tag>
#        ./projectm-source.sh v4.1.0

git clone https://github.com/projectM-visualizer/projectm
cd projectm
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz projectm.tar.gz projectm/*
rm -rf projectm
