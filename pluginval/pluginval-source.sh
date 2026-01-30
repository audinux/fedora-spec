#!/bin/bash

# Usage: ./pluginval-source.sh <TAG>
#        ./pluginval-source.sh v1.0.4

git clone https://github.com/Tracktion/pluginval/
cd pluginval
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz pluginval.tar.gz pluginval/*
rm -rf pluginval
