#!/bin/bash

# To get Enover source code:
# ./envoer-source.sh v1.0
git clone https://github.com/chmaha/Enover
cd Enover
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Enover.tar.gz Enover/*
rm -rf Enover
