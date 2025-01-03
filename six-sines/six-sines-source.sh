#!/bin/bash

# Usage: ./six-sines-source.sh <TAG>
#        ./six-sines-source.sh v0.99

git clone https://github.com/baconpaul/six-sines
cd six-sines
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz six-sines.tar.gz six-sines/*
rm -rf six-sines
