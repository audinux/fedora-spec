#!/bin/bash

# Usage: ./camomile-source.sh <TAG>
# ./camomile-source.sh v1.0.7

git clone https://github.com/pierreguillot/Camomile
cd Camomile
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Camomile.tar.gz Camomile/*
rm -rf Camomile
