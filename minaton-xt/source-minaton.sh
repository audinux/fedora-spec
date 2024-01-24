#!/bin/bash

# Usage: ./source-minaton.sh <tag>
#        ./source-minaton.sh 0.2.0

git clone https://github.com/AnClark/Minaton-XT
cd Minaton-XT
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Minaton-XT.tar.gz Minaton-XT/*
rm -rf Minaton-XT
