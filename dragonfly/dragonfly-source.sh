#!/bin/bash

# Usage: ./source.sh <TAG>
# ./dragonfly-source.sh 3.2.5

git clone https://github.com/michaelwillis/dragonfly-reverb
cd dragonfly-reverb
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz dragonfly-reverb.tar.gz dragonfly-reverb/*
rm -rf dragonfly-reverb

