#!/bin/bash

# ./starling-via-source.sh <tag>
# ./starling-via-source.sh v0.6.0

git clone --recursive https://github.com/starlingcode/Via-for-Rack.git
cd Via-for-Rack
git checkout $1
git submodule init
git submodule update
find . -name ".git" -exec rm -rf {} \;
cd ..
tar cvfz Via-for-Rack.tar.gz Via-for-Rack
rm -rf Via-for-Rack
