#!/bin/bash

# Usage: ./guitarmidi-lv2-sources.sh <TAG>
# ./guitarmidi-lv2-sources.sh v1.1

git clone https://github.com/geraldmwangi/GuitarMidi-LV2
cd GuitarMidi-LV2
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz GuitarMidi-LV2.tar.gz GuitarMidi-LV2/*
rm -rf GuitarMidi-LV2
