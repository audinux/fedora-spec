#!/bin/bash

# Usage: ./delirion-sources.sh <TAG>
#        ./delirion-sources.sh master

git clone https://github.com/igorski/delirion
cd delirion
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress

git clone https://github.com/juce-framework/JUCE
cd JUCE
git checkout 8.0.1
cd ..

find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz delirion.tar.gz delirion/*
rm -rf delirion
