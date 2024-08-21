#!/bin/bash

# Usage: ./bambootracker_source.sh <TAG>
# ./bambootracker_source.sh v0.4.6

git clone https://github.com/rerrahkr/BambooTracker
cd BambooTracker
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz BambooTracker.tar.gz BambooTracker/*
rm -rf BambooTracker

