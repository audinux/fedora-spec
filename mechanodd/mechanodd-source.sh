#!/bin/bash

# Usage: ./mechanodd-source.sh <TAG>
#        ./mechanodd-source.sh v0.2.0

git clone https://github.com/odoare/Mechanodd
cd Mechanodd
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress

git clone --depth=1 -b 8.0.12  https://github.com/juce-framework/JUCE

find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Mechanodd.tar.gz Mechanodd/*
rm -rf Mechanodd
