#!/bin/bash

# Usage: ./maim-sources.sh <TAG>
#        ./maim-sources.sh v1.9.9

git clone --depth=1 https://github.com/ArdenButterfield/Maim
cd Maim
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Maim.tar.gz Maim/*
rm -rf Maim
