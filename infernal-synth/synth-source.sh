#!/bin/bash

# Usage: ./synth-source.sh <PROJECT> <TAG>
#        ./synth-source.sh firefly-synth 75b98515ba51665525dacd545e8e050a8b38bd96

git clone https://github.com/sjoerdvankreel/$1/
cd $1
git checkout $2
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
