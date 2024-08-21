#!/bin/bash

# ./rack-source.sh <tag>
# ./rack-source.sh v2.2.1

git clone https://github.com/VCVRack/Rack.git Rack
cd Rack
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name ".git" -exec rm -rf {} \;
cd ..
tar cvfz Rack.tar.gz Rack/*
rm -rf Rack
