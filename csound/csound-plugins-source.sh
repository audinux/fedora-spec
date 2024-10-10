#!/bin/bash

# Usage: ./csound-plugins-source.sh <TAG>
#        ./csound-plugins-source.sh v1.0.2

git clone https://github.com/csound/plugins
cd plugins
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz plugins.tar.gz plugins/*
rm -rf plugins
