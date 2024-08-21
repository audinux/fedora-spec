#!/bin/bash

# Usage: ./stargate-source.sh <TAG>
# ./stargate-source.sh release-23.03.1

git clone https://github.com/stargatedaw/stargate
cd stargate
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz stargate.tar.gz stargate/*
rm -rf stargate
