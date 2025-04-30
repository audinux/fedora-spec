#!/bin/bash

# Usage: ./distrho-ports-source.sh <tag>
#        ./distrho-ports-source.sh master

git clone https://github.com/DISTRHO/DISTRHO-Ports
cd DISTRHO-Ports
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz DISTRHO-Ports.tar.gz DISTRHO-Ports/*
rm -rf DISTRHO-Ports
