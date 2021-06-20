#!/bin/bash

# Usage:
# ./klystrack-source <TAG>
# ./klystrack-source 1.7.6

git clone https://github.com/kometbomb/klystrack.git
cd klystrack
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz klystrack.tar.gz klystrack/*
rm -rf klystrack
