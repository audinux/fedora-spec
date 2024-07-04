#!/bin/bash

# Usage: ./xenos-source.sh <TAG>
# .       /xenos-source.sh main

git clone https://github.com/raphaelradna/xenos
cd xenos
git checkout $1
git submodule update --init --recursive

git clone https://github.com/juce-framework/JUCE.git
cd JUCE
git checkout 7.0.9
cd ..

find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz xenos.tar.gz xenos/*
rm -rf xenos
