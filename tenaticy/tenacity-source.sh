#!/bin/bash

# Usage: ./tenacity-sources.sh <TAG>
#        ./tenacity-source.sh v1.3.4

git clone https://codeberg.org/tenacityteam/tenacity.git
cd tenacity
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz tenacity.tar.gz tenacity/*
rm -rf tenacity
