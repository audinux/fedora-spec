#!/bin/bash

# Usage: ./resonarium-source.sh <tag>
#        ./resonarium-source.sh master

git clone https://github.com/gabrielsoule/resonarium
cd resonarium
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz resonarium.tar.gz resonarium/*
rm -rf resonarium
