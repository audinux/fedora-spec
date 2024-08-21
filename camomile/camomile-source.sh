#!/bin/bash

# Usage: ./camomile-source.sh <TAG>
# ./camomile-source.sh v1.0.7

git clone https://github.com/pierreguillot/Camomile
cd Camomile
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Camomile.tar.gz Camomile/*
rm -rf Camomile
