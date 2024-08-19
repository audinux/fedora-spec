#!/bin/bash

# Usage: ./vst3sdk-source.sh <tag>
#        ./vst3sdk-source.sh v3.7.8_build_34

git clone https://github.com/steinbergmedia/vst3sdk
cd vst3sdk
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz vst3sdk.tar.gz vst3sdk/*
rm -rf vst3sdk
