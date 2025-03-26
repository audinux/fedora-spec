#!/bin/bash

# Usage: ./stegosaurus-sources.sh <TAG>
#        ./stegosaurus-sources.sh main

git clone https://github.com/thunderox/stegosaurus/
cd stegosaurus
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz stegosaurus.tar.gz stegosaurus/*
rm -rf stegosaurus
