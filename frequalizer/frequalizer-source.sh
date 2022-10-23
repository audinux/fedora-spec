#!/bin/bash

# Usage: ./frequalizer-source.sh <TAG>
# ./frequalizer-source.sh master

git clone https://github.com/ffAudio/Frequalizer
cd Frequalizer
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Frequalizer.tar.gz Frequalizer/*
rm -rf Frequalizer

