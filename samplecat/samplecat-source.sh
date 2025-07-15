#!/bin/bash

# Usage: ./samplecat-source.sh <TAG>
#        ./samplecat-source.sh v0.3.4

git clone https://github.com/ayyi/samplecat
cd samplecat
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz samplecat.tar.gz samplecat/*
rm -rf samplecat
