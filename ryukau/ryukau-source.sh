#!/bin/bash

# ./ryukau-source.sh <tag>
# ./ryukau-source.sh master

git clone --recursive https://github.com/Wasted-Audio/ryukau_LV2Plugins
cd ryukau_LV2Plugins
find . -name .git -exec rm -rf {} \;
cd ..
mv ryukau_LV2Plugins ryukau
tar cvfz ryukau.tar.gz ryukau/*
rm -rf ryukau
