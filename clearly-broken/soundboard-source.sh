#!/bin/bash

# Usage: ./soundboard-source.sh <TAG>
# ./soundboard-source.sh c2447333286dad81bdcd73a25e481c3bfdab58e3

git clone https://github.com/clearly-broken-software/SoundBoard/
cd SoundBoard
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz SoundBoard.tar.gz SoundBoard/*
rm -rf SoundBoard
