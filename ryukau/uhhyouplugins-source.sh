#!/bin/bash

# ./uhhyouplugins-source.sh <tag>
# ./uhhyouplugins-source.sh e5eee4c3

git clone --recursive https://github.com/ryukau/VSTPlugins
cd VSTPlugins
find . -name .git -exec rm -rf {} \;
cd ..
mv VSTPlugins
tar cvfz VSTPlugins.tar.gz VSTPlugins/*
rm -rf VSTPlugins
