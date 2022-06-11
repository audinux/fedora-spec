#!/bin/bash

# Usage: ./odin-sources.sh <TAG>
# ./odin-sources.sh v2.3.2

git clone https://github.com/TheWaveWarden/odin2
cd odin2
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz odin2.tar.gz odin2/*
rm -rf odin2

git clone -b lv2 https://github.com/lv2-porting-project/JUCE/ JUCELV2
cd JUCELV2
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz JUCELV2.tar.gz JUCELV2/*
rm -rf JUCELV2
