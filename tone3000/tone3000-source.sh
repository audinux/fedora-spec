#!/bin/bash

# Usage: ./tone3000-source.sh <TAG>
#        ./tone3000-source.sh v0.0.11

git clone https://github.com/tone-3000/tone3000-plugin/
cd tone3000-plugin
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
if [ $? -ne 0 ]; then
    echo "Problem with submodules"
    exit 1
fi
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz tone3000-plugin.tar.gz tone3000-plugin/*
rm -rf tone3000-plugin
