#!/bin/bash

# ./uhhyouplugins-source.sh <tag>
# ./uhhyouplugins-source.sh e5eee4c3

git clone https://github.com/ryukau/VSTPlugins
cd VSTPlugins
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
mv VSTPlugins
tar cvfz VSTPlugins.tar.gz VSTPlugins/*
rm -rf VSTPlugins
