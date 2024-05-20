#!/bin/bash

# Usage: ./cetone-sources.sh <TAG>
#        ./cetone-sources.sh master

git clone https://github.com/AnClark/CetoneSynth
cd CetoneSynth
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz CetoneSynth.tar.gz CetoneSynth/*
rm -rf CetoneSynth
