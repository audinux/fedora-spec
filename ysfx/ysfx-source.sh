#!/bin/bash

# To get adlplug source code: ./ysfx-source master
# git clone https://github.com/jpcima/ysfx
git clone https://github.com/JoepVanlier/ysfx
cd ysfx
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ysfx.tar.gz ysfx/*
rm -rf ysfx
