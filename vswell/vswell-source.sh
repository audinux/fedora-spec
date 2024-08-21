#!/bin/bash

# ./vswell-source.sh <tag>
# ./vswell-source.sh v0.3.0

git clone https://github.com/GModal/vSwell
cd vSwell
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
rm -rf .git dpf/.git
cd ..
tar cvfz vSwell.tar.gz vSwell/*
rm -rf vSwell
