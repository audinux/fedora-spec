#!/bin/bash

# Usage: ./audio-effects-sources.sh <TAG>
# ./audio-effects-sources.sh v1.0.0

git clone https://github.com/juandagilc/Audio-Effects
cd Audio-Effects
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Audio-Effects.tar.gz Audio-Effects/*
rm -rf Audio-Effects
