#!/bin/bash

# Usage: ./source-furnace.sh <tag>
#        ./source-furnace.sh v0.5.8

git clone https://github.com/tildearrow/furnace
cd furnace
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz furnace.tar.gz furnace/*
rm -rf furnace
