#!/bin/bash

# Usage: ./sg323-sources.sh <TAG>
#        ./sg323-sources.sh 0.6.3

git clone https://github.com/greyboxaudio/SG-323
cd SG-323
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz SG-323.tar.gz SG-323/*
rm -rf SG-323
