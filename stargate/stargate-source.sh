#!/bin/bash

# Usage: ./stargate-source.sh <TAG>
# ./stargate-source.sh release-23.03.1

git clone https://github.com/stargatedaw/stargate
cd stargate
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz stargate.tar.gz stargate/*
rm -rf stargate
