#!/bin/bash

# ./rack-source.sh <tag>
# ./rack-source.sh v2.1.2

git clone https://github.com/VCVRack/Rack.git Rack
cd Rack
git checkout $1
git submodule init
git submodule update
find . -name ".git" -exec rm -rf {} \;
cd ..
tar cvfz Rack.tar.gz Rack/*
rm -rf Rack
