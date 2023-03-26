#!/bin/bash

# Usage: ./source-zynayumi.sh <tag>
#        ./source-zynayumi.sh master

git clone https://github.com/zynayumi/zynayumi
cd zynayumi
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz zynayumi.tar.gz zynayumi/*
rm -rf zynayumi
