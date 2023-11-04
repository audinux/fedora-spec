#!/bin/bash

# Usage: ./fxseq-source.sh <TAG>
# ./fxseq-source.sh master

git clone https://github.com/ssabug/fxseq
cd fxseq
git checkout $1
git submodule update --init --recursive --progress
git clone https://github.com/juce-framework/JUCE
cd JUCE
git checkout 7.0.7
cd ..
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz fxseq.tar.gz fxseq/*
rm -rf fxseq
