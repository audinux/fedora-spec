#!/bin/bash

# Usage: ./aidadsp-lv2-source.sh <TAG>
# ./aidadsp-lv2-source.sh v0.95

git clone https://github.com/moddevices/aidadsp-lv2
cd aidadsp-lv2
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz aidadsp-lv2.tar.gz aidadsp-lv2/*
rm -rf aidadsp-lv2
