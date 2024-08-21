#!/bin/bash

# Usage: ./source-splash.sh <tag>
#        ./source-splash.sh v8.9.40

git clone https://gitlab.com/splashmapper/splash
cd splash
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz splash.tar.gz splash/*
rm -rf splash
