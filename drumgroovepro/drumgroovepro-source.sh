#!/bin/bash

# Usage: ./drumgroovepro-source.sh <TAG>
#        ./drumgroovepro-source.sh v0.9.5

git clone https://github.com/InToEtherion/DrumGroovePro
cd DrumGroovePro
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress

git clone https://github.com/juce-framework/JUCE.git
cd JUCE
git checkout 8.0.10
git submodule update --depth=1 --init --recursive --progress
cd ..

find . -name .git -exec rm -rf {} \;

cd ..
tar cvfz DrumGroovePro.tar.gz DrumGroovePro/*
rm -rf DrumGroovePro
