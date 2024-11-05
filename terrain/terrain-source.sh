#!/bin/bash

# Usage: ./terrain-source.sh <TAG>
#        ./terrain-source.sh 1.2.2

git clone https://github.com/aaronaanderson/Terrain
cd Terrain
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Terrain.tar.gz Terrain/*
rm -rf Terrain
