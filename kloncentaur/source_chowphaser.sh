#!/bin/bash

# Usage: ./source_chowphaser.sh <tag>
#        ./source_chowphaser.sh 1.1.1

git clone --recursive https://github.com/jatinchowdhury18/ChowPhaser
cd ChowPhaser
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ChowPhaser.tar.gz ChowPhaser/*
rm -rf ChowPhaser
