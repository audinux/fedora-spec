#!/bin/bash

# Usage: ./sfxr-qt-source.sh <TAG>
#        ./sfxr-qt-source.sh 1.5.0

git clone https://github.com/agateau/sfxr-qt
cd sfxr-qt
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz sfxr-qt.tar.gz sfxr-qt/*
rm -rf sfxr-qt
