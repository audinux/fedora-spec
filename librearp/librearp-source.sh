#!/bin/bash

# Usage: ./librearp-source.sh <TAG>
#        ./librearp-source.sh 2.5

git clone https://gitlab.com/LibreArp/LibreArp LibreArpLV2
cp -r LibreArpLV2 LibreArpVST3
cd LibreArpLV2
git checkout $1-lv2
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz LibreArpLV2.tar.gz LibreArpLV2/*
rm -rf LibreArpLV2

cd LibreArpVST3
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz LibreArpVST3.tar.gz LibreArpVST3/*
rm -rf LibreArpVST3
