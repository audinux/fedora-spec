#!/bin/bash

git clone https://github.com/timothyschoen/PlugData
cd PlugData
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz PlugData.tar.gz PlugData/*
rm -rf PlugData
