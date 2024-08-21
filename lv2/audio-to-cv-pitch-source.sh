#!/bin/bash

# Usage: ./audio-to-cv-pitch-source.sh <TAG>
# ./audio-to-cv-pitch-source.sh v0.95

git clone https://github.com/BramGiesen/audio-to-cv-pitch-lv2
cd audio-to-cv-pitch-lv2
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz audio-to-cv-pitch-lv2.tar.gz audio-to-cv-pitch-lv2/*
rm -rf audio-to-cv-pitch-lv2
