#!/bin/bash

# Usage: ./hydrogen-source.sh <TAG>
#        ./hydrogen-source.sh 1.2.5

git clone https://github.com/hydrogen-music/hydrogen
cd hydrogen
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz hydrogen.tar.gz hydrogen/*
rm -rf hydrogen
