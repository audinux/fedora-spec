#!/bin/bash

# To get si-plugins source code:
# ./si-plugins-source.sh v0.3.0
git clone https://github.com/guysherman/si-plugins
cd si-plugins
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz si-plugins.tar.gz si-plugins/*
rm -rf si-plugins
