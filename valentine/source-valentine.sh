#!/bin/bash

# Usage: ./source-valentine.sh <tag>
#        ./source-valentine.sh v00.0.4

git clone https://github.com/tote-bag-labs/valentine
cd valentine
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz valentine.tar.gz valentine/*
rm -rf valentine
