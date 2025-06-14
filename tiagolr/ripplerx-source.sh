#!/bin/bash

# Usage: ./ripplerx-source.sh <TAG>
#        ./ripplerx-source.sh v1.1.1

git clone https://github.com/tiagolr/ripplerx
cd ripplerx
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ripplerx.tar.gz ripplerx/*
rm -rf ripplerx
