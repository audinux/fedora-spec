#!/bin/bash

# Usage: ./iem-plugins-sources.sh <TAG>
#        ./iem-plugins-sources.sh v1.14.1

git clone  https://git.iem.at/audioplugins/IEMPluginSuite
cd IEMPluginSuite
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz IEMPluginSuite.tar.gz IEMPluginSuite/*
rm -rf IEMPluginSuite
