#!/bin/bash

# Usage: ./qpitch-source.sh <TAG>
#        ./qpitch-source.sh v1.2.1-fixed

git clone https://github.com/skynse/qpitch
cd qpitch
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz qpitch.tar.gz qpitch/*
rm -rf qpitch
