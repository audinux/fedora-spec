#!/bin/bash

# Usage: ./clearly-broken-source.sh <PROJECT> <TAG>
# ./clearly-broken-source.sh boomer 1916d46a2823d0f091edf545666058456c93b004

git clone https://github.com/clearly-broken-software/$1
cd $1
git checkout $2
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
