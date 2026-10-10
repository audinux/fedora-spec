#!/bin/bash

# Usage: ./open-riff-box-source.sh <TAG>
#        ./open-riff-box-source.sh v0.9.1

git clone https://github.com/dlujic/open-riff-box
cd open-riff-box
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
if [ $? -ne 0 ]; then
    echo "Problem with submodules"
    exit 1
fi
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz open-riff-box.tar.gz open-riff-box/*
rm -rf open-riff-box
