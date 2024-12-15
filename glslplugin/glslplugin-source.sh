#!/bin/bash

# Usage: ./glslplugin-source.sh <TAG>
#        ./glslplugin-source.sh next

git clone https://github.com/COx2/glslEditor_AudioPlugin/
cd glslEditor_AudioPlugin
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;

rm -rf Prebuilt
rm -rf Projucer

cd ..
tar cvfz glslEditor_AudioPlugin.tar.gz glslEditor_AudioPlugin/*
rm -rf glslEditor_AudioPlugin
