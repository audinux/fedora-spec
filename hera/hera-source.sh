#!/bin/bash

# ./hera-source.sh <tag>
# ./hera-source.sh f6fe5b900f4cf84809686466e0a37de5edf008fd

git clone https://github.com/jpcima/Hera
cd Hera
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Hera.tar.gz Hera/*
rm -rf Hera
