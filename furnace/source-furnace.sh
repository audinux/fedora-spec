#!/bin/bash

# Usage: ./source-furnace.sh <tag>
#        ./source-furnace.sh v0.5.8

git clone https://github.com/tildearrow/furnace
cd furnace
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz furnace.tar.gz furnace/*
rm -rf furnace
