#!/bin/bash

# Usage: ./source-furnace.sh <tag>
#        ./source-furnace.sh v0.5.8

git clone --depth=1 https://github.com/tildearrow/furnace
cd furnace
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz furnace.tar.gz furnace/*
rm -rf furnace
