#!/bin/bash

# Usage: ./uprising-source.sh <TAG>
# ./uprising-source.sh 89f5b49d90cd47611da7e7dc2009061768716b4c

git clone https://github.com/clearly-broken-software/Uprising/
cd Uprising
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Uprising.tar.gz Uprising/*
rm -rf Uprising
