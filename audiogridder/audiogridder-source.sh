#!/bin/bash

# Usage: ./audiogridder-source.sh <TAG>
#        ./audiogridder-source.sh v1.2.0

git clone https://github.com/apohl79/audiogridder
cd audiogridder
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz audiogridder.tar.gz audiogridder/*
rm -rf audiogridder
