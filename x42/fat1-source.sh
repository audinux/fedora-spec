#!/bin/bash

# ./fat1-source.sh <tag>
# ./fat1-source.sh v0.7.0

git clone https://github.com/x42/fat1.lv2
cd fat1.lv2
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz fat1.lv2.tar.gz fat1.lv2/*
rm -rf fat1.lv2
