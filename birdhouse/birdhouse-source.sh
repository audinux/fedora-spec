#!/bin/bash

# Usage: ./birdhouse-source.sh <TAG>
#        ./birdhouse-source.sh v0.1.2

git clone https://github.com/madskjeldgaard/Birdhouse
cd Birdhouse
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Birdhouse.tar.gz Birdhouse/*
rm -rf Birdhouse
