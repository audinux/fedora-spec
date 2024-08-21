#!/bin/bash

# To get RCComp source code:
# ./rccomp-source.sh v0.9
git clone https://github.com/chmaha/RCComp
cd RCComp
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz RCComp.tar.gz RCComp/*
rm -rf RCComp
