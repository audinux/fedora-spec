#!/bin/bash

# Usage: ./source_chowmatrix.sh <tag>
#        ./source_chowmatrix.sh 1.2.0

git clone --recursive https://github.com/Chowdhury-DSP/ChowMatrix
cd ChowMatrix
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ChowMatrix.tar.gz ChowMatrix/*
rm -rf ChowMatrix
