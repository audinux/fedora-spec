#!/bin/bash

# ./rack-source.sh <tag>
# ./rack-source.sh v1.1.6

git clone https://github.com/VCVRack/Rack.git Rack
cd Rack
git checkout $1
git submodule update --init --recursive --progress
find . -name ".git" -exec rm -rf {} \;
cd dep
wget https://vcvrack.com/downloads/dep/pffft.zip
unzip pffft.zip
mkdir include
cp pffft/*.h include/
mv pffft jpommier-pffft-rack 
rm  pffft.zip
cd ../..
tar cvfz Rack.tar.gz Rack/*
rm -rf Rack
