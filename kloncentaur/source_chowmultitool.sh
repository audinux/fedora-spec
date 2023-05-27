#!/bin/bash

# Usage: ./source_chowmultitool.sh <tag>
#        ./source_chowmultitool.sh v1.0.0

git clone --recursive https://github.com/Chowdhury-DSP/ChowMultiTool
cd ChowMultiTool
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ChowMultiTool.tar.gz ChowMultiTool/*
rm -rf ChowMultiTool
