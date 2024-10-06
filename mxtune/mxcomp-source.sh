#!/bin/bash

# Usage: ./mxcomp-source.sh <TAG>
#        ./mxcomp-source.sh v0.9.8

git clone https://github.com/liuanlin-mx/MXComp
cd MXComp
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz MXComp.tar.gz MXComp/*
rm -rf MXComp
