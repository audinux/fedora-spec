#!/bin/bash

# Usage: ./source-smartguitarpro.sh <tag>
#        ./source-smartguitarpro.sh master

git clone https://github.com/GuitarML/SmartAmpPro
cd SmartAmpPro
# git checkout origin/release/$1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz SmartAmpPro.tar.gz SmartAmpPro/*
rm -rf SmartAmpPro
