#!/bin/bash

# Usage: ./frequalizer-source.sh <TAG>
# ./frequalizer-source.sh master

git clone https://github.com/ffAudio/Frequalizer
cd Frequalizer
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Frequalizer.tar.gz Frequalizer/*
rm -rf Frequalizer

