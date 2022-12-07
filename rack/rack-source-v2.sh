#!/bin/bash

# ./rack-source.sh <tag>
# ./rack-source.sh v2.2.1

git clone https://github.com/VCVRack/Rack.git Rack
cd Rack
git checkout $1
git submodule update --init --recursive
find . -name ".git" -exec rm -rf {} \;
cd ..
tar cvfz Rack.tar.gz Rack/*
rm -rf Rack
