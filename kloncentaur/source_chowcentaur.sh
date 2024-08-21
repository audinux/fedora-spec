#!/bin/bash

# Usage: ./source_chowcentaur.sh <tag>
#        ./source_chowcentaur.sh 1.4.0

git clone --recursive https://github.com/jatinchowdhury18/KlonCentaur
cd KlonCentaur
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz KlonCentaur.tar.gz KlonCentaur/*
rm -rf KlonCentaur
