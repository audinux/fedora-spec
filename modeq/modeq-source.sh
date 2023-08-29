#!/bin/bash

# ./modeq-source.sh <tag>
# ./modeq-source.sh v0.4.0

git clone https://github.com/tobanteAudio/modEQ
cd modEQ
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz modEQ.tar.gz modEQ/*
rm -rf modEQ
