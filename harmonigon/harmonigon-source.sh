#!/bin/bash

# Usage: ./harmonigon-source.sh <TAG>
#        ./harmonigon-source.sh master

git clone https://github.com/StrangeLoopsAudio/Harmonigon
cd Harmonigon
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Harmonigon.tar.gz Harmonigon/*
rm -rf Harmonigon

