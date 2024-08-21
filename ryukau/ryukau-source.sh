#!/bin/bash

# ./ryukau-source.sh <tag>
# ./ryukau-source.sh master

git clone https://github.com/Wasted-Audio/ryukau_LV2Plugins
cd ryukau_LV2Plugins
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
mv ryukau_LV2Plugins ryukau
tar cvfz ryukau.tar.gz ryukau/*
rm -rf ryukau
