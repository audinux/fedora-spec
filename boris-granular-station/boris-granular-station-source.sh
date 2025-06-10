#!/bin/bash

# Usage: ./boris-granular-station-source.sh <tag>
#        ./boris-granular-station-source.sh master

git clone https://github.com/glesdora/boris-granular-station
cd boris-granular-station
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz boris-granular-station.tar.gz boris-granular-station/*
rm -rf boris-granular-station
