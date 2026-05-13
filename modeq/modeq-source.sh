#!/bin/bash

# ./modeq-source.sh <tag>
# ./modeq-source.sh v0.4.0

git clone --depth=1 https://github.com/tobanteAudio/modEQ
cd modEQ
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz modEQ.tar.gz modEQ/*
rm -rf modEQ
