#!/bin/bash

# ./bespokesynth-sources.sh <tag>
# ./bespokesynth-sources.sh v1.0.999

git clone https://github.com/BespokeSynth/BespokeSynth
cd BespokeSynth
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz BespokeSynth.tar.gz BespokeSynth/*
rm -rf BespokeSynth
