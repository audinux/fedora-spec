#!/bin/bash

# Usage: ./shoopdaloop-source.sh <TAG>
# ./shoopdaloop-source.sh v0.95

git clone https://github.com/SanderVocke/shoopdaloop
cd shoopdaloop
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz shoopdaloop.tar.gz shoopdaloop/*
rm -rf shoopdaloop
