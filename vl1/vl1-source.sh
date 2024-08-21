#!/bin/bash

# ./vl1-source.sh <tag>
# ./vl1-source.sh 1.1.0.0

git clone https://github.com/linuxmao-org/VL1-emulator
cd VL1-emulator
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
rm -rf .git dpf/.git
cd ..
tar cvfz VL1-emulator.tar.gz VL1-emulator/*
rm -rf VL1-emulator
