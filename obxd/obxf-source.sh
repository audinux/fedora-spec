#!/bin/bash

# Usage: ./obxf-source.sh <TAG>
#        ./obxf-source.sh v1.0.0

git clone --depth=1 https://github.com/surge-synthesizer/OB-Xf
cd OB-Xf
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz OB-Xf.tar.gz OB-Xf/*
rm -rf OB-Xf
