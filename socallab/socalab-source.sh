#!/bin/bash

# Usage: ./socalab-source.sh <TAG>
# ./socalab-source.sh master

git clone --recursive https://github.com/FigBug/slPlugins
cd slPlugins
git checkout $1
git submodules update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz slPlugins.tar.gz slPlugins/*
rm -rf slPlugins
