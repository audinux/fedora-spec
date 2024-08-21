#!/bin/bash

# Usage: ./guitarmidi-lv2-source.sh <TAG>
# ./guitarmidi-lv2-source.sh 1.1

git clone https://github.com/geraldmwangi/GuitarMidi-LV2
cd GuitarMidi-LV2
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz GuitarMidi-LV2.tar.gz GuitarMidi-LV2/*
rm -rf GuitarMidi-LV2
