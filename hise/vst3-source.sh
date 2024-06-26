#!/bin/bash

# Usage: ./vst3-source.sh <TAG>
#        ./vst3-source.sh v3.7.11_build_10

git clone https://github.com/steinbergmedia/vst3sdk
cd vst3sdk
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz vst3sdk.tar.gz vst3sdk/*
rm -rf vst3sdk
