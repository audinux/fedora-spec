#!/bin/bash

# To get adlplug source code: ./adlplug-source v1.0.2
git clone https://github.com/jpcima/ADLplug
cd ADLplug
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ADLplug.tar.gz ADLplug/*
rm -rf ADLplug
