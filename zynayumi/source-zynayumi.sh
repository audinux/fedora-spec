#!/bin/bash

# Usage: ./source-zynayumi.sh <tag>
#        ./source-zynayumi.sh master

git clone https://github.com/zynayumi/zynayumi
cd zynayumi
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz zynayumi.tar.gz zynayumi/*
rm -rf zynayumi
