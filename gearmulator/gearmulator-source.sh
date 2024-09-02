#!/bin/bash

# Usage: ./gearmulator-source.sh <TAG>
#        ./gearmulator-source.sh main

git clone https://github.com/dsp56300/gearmulator
cd gearmulator
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz gearmulator.tar.gz gearmulator/*
rm -rf gearmulator
