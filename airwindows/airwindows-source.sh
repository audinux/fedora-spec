#!/bin/bash

# Usage: ./airwindows-source.sh <TAG>
# ./airwindows-source.sh master

git clone https://github.com/airwindows/airwindows
cd airwindows
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
rm -rf plugins/MacAU
rm -rf plugins/MacSignedAU
rm -rf plugins/MacSignedVST
rm -rf plugins/MacVST
rm -rf plugins/WinVST
cd ..
tar cvfz airwindows.tar.gz airwindows/*
rm -rf airwindows
