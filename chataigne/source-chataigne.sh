#!/bin/bash

# Usage: ./source-chataigne.sh <tag>
#        ./source-chataigne.sh 1.9.5b11

git clone https://github.com/benkuper/Chataigne
cd Chataigne
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Chataigne.tar.gz Chataigne/*
rm -rf Chataigne
