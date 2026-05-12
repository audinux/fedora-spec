#!/bin/bash

# Usage: ./spicefx-source.sh <TAG>
#        ./spicefx-source.sh main

git clone https://github.com/DatanoiseTV/spice-oss
cd spice-oss
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz spice-oss.tar.gz spice-oss/*
rm -rf spice-oss
