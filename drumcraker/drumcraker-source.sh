#!/bin/bash

# Usage: ./drumcraker-source.sh <TAG>
#        ./drumcraker-source.sh v1.2.0

git clone https://github.com/Wamphyre/DrumCraker/
cd DrumCraker
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi

git submodule update --init --recursive --progress

git clone --depth 1 --branch 7.0.12 https://github.com/juce-framework/JUCE.git

find . -name .git -exec rm -rf {} \;

cd ..
tar cvfz DrumCraker.tar.gz DrumCraker/*
rm -rf DrumCraker
