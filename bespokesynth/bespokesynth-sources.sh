#!/bin/bash

# ./bespokesynth-sources.sh <tag>
# ./bespokesynth-sources.sh v1.0.999

git clone -b $1 --recursive https://github.com/BespokeSynth/BespokeSynth
cd BespokeSynth
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz BespokeSynth.tar.gz BespokeSynth/*
rm -rf BespokeSynth
