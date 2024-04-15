#!/bin/bash

# Usage: ./giada-source.sh <TAG>
#        ./giada-source.sh v1.0.0

git clone https://github.com/monocasual/giada
cd giada
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz giada.tar.gz giada/*
rm -rf giada
