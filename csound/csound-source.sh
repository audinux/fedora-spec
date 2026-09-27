#!/bin/bash

# Usage: ./csound-source.sh <TAG>
#        ./csound-source.sh 7.0.0-beta.17

git clone https://github.com/csound/csound
cd csound
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
if [ $? -ne 0 ]; then
    echo "Problem with submodules"
    exit 1
fi
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz csound.tar.gz csound/*
rm -rf csound
