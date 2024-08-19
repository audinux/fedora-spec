#!/bin/bash

# Usage: ./source_chowcentaur.sh <tag>
#        ./source_chowcentaur.sh 1.4.0

git clone --recursive https://github.com/jatinchowdhury18/KlonCentaur
cd KlonCentaur
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz KlonCentaur.tar.gz KlonCentaur/*
rm -rf KlonCentaur
