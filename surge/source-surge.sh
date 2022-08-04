#!/bin/bash

# Usage: ./source-surge.sh <tag>
#        ./source-surge.sh release_xt_1.0.0
#        ./source-surge.sh origin/release/1.9.0

git clone https://github.com/surge-synthesizer/surge
cd surge
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz surge.tar.gz surge/*
rm -rf surge
