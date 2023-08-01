#!/bin/bash

# Usage: ./vst3-source.sh <TAG>
#        ./vst3-source.sh v3.7.8_build_34

git clone --recursive https://github.com/steinbergmedia/vst3sdk
find vst3dsk -name .git -exec rm -rf {} \;
tar cvfz vst3sdk.tar.gz vst3sdk/*
rm -rf vst3sdk

