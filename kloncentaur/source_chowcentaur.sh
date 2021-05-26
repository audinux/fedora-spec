#!/bin/bash

# Usage: ./source_chowcentaur.sh <tag>
#        ./source_chowcentaur.sh 1.4.0

git clone --recursive https://github.com/jatinchowdhury18/KlonCentaur
cd KlonCentaur
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz KlonCentaur.tar.gz KlonCentaur/*
rm -rf KlonCentaur
