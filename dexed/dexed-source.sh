#!/bin/bash

# Usage: ./dexed-source.sh <TAG>
#        ./dexed-source.sh v0.9.6

git clone https://github.com/asb2m10/dexed
cd dexed
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz dexed.tar.gz dexed/*
rm -rf dexed
