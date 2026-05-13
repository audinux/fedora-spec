#!/bin/bash

# Usage: ./source-chataigne.sh <tag>
#        ./source-chataigne.sh 1.9.5b11

git clone --depth=1 https://github.com/benkuper/Chataigne
cd Chataigne
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Chataigne.tar.gz Chataigne/*
rm -rf Chataigne

git clone --depth=1 --branch=develop-local http://github.com/benkuper/JUCE
find JUCE -name .git -exec rm -rf {} \;
tar cvfz JUCE.tar.gz JUCE/*
rm -rf JUCE
