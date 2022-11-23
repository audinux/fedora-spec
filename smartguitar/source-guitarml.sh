#!/bin/bash

# Usage: ./source-smartguitarpro.sh <tag>
#        ./source-smartguitarpro.sh v1.3

git clone https://github.com/GuitarML/SmartGuitarAmp
cd SmartGuitarAmp
git checkout origin/release/$1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz SmartGuitarAmp.tar.gz SmartGuitarAmp/*
rm -rf SmartGuitarAmp
