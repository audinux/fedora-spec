#!/bin/bash

# Usage: ./dsp4guitar-source.sh <TAG>
#        ./dsp4guitar-source.sh 1.1

git clone https://github.com/GizzZmo/DSP4Guitar
cd DSP4Guitar
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
git clone --depth 1 --branch 7.0.9 https://github.com/juce-framework/JUCE.git
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz DSP4Guitar.tar.gz DSP4Guitar/*
rm -rf DSP4Guitar
