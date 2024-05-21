#!/bin/bash

# Usage: ./cetone-source.sh <PROJECT> <TAG>
#        ./cetone-source.sh CetoneSynth master

git clone https://github.com/AnClark/$1
cd $1
git checkout $2
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
