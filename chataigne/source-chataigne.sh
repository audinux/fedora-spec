#!/bin/bash

# Usage: ./source-chataigne.sh <tag>
#        ./source-chataigne.sh 1.9.5b11

git clone https://github.com/benkuper/Chataigne
cd Chataigne
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Chataigne.tar.gz Chataigne/*
rm -rf Chataigne

git clone --branch=develop-local http://github.com/benkuper/JUCE
find JUCE -name .git -exec rm -rf {} \;
tar cvfz JUCE.tar.gz JUCE/*
rm -rf JUCE
