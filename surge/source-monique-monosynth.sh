#!/bin/bash

# Usage: ./source-monique-monosynth.sh <tag>
#        ./source-monique-monosynth.sh main

git clone https://github.com/surge-synthesizer/monique-monosynth
cd monique-monosynth
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz monique-monosynth.tar.gz monique-monosynth/*
rm -rf monique-monosynth
