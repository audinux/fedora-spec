#!/bin/bash

# Usage: ./amsynth-source.sh <TAG>
#        ./amsynth-source.sh release-2.0.0

git clone https://github.com/amsynth/amsynth
cd amsynth
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz amsynth.tar.gz amsynth/*
rm -rf amsynth
