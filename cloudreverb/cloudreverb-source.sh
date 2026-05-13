#!/bin/bash

# Usage: ./cloudreverb-source.sh <TAG>
#        ./cloudreverb-source.sh master

git clone --depth=1 https://github.com/xunil-cloud/CloudReverb/
cd CloudReverb
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz CloudReverb.tar.gz CloudReverb/*
rm -rf CloudReverb
