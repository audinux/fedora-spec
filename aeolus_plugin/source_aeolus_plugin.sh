#!/bin/bash

# Usage: ./source_aeolus_plugin.sh <tag>
#        ./source_aeolus_plugin.sh v0.1.12

git clone https://github.com/Archie3d/aeolus_plugin
cd aeolus_plugin
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz aeolus_plugin.tar.gz aeolus_plugin/*
rm -rf aeolus_plugin
