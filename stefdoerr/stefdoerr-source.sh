#!/bin/bash

# Usage: ./stefdoerr-source.sh <PROJECT> <TAG>
#        ./stefdoerr-source.sh sitar v0.0.6

git clone https://github.com/stefdoerr/$1/
cd $1
git checkout $2
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $2"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
