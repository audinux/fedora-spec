#!/bin/bash

# Usage: ./vst3-source <TAG>
# ./vst3-source master

git clone --recursive https://github.com/steinbergmedia/vst3sdk
find vst3dsk -name .git -exec rm -rf {} \;
tar cvfz vst3sdk.tar.gz vst3sdk/*
rm -rf vst3dsk
