#!/bin/bash

# ./string-machine-source.sh <tag>
# ./string-machine-source.sh master

git clone --depth=1 https://github.com/jpcima/string-machine
cd string-machine
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz string-machine.tar.gz string-machine/*
rm -rf string-machine
