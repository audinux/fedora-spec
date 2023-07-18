#!/bin/bash

# Usage: ./harmonigon-source.sh <TAG>
#        ./harmonigon-source.sh master

git clone https://github.com/StrangeLoopsAudio/Harmonigon
cd Harmonigon
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Harmonigon.tar.gz Harmonigon/*
rm -rf Harmonigon

