#!/bin/bash

# Usage: ./vimix-source.sh <TAG>
#        ./vimix-source.sh 0.9.0

git clone https://github.com/brunoherbelin/vimix
cd vimix
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz vimix.tar.gz vimix/*
rm -rf vimix
