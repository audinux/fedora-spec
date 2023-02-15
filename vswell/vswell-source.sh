#!/bin/bash

# ./vswell-source.sh <tag>
# ./vswell-source.sh v0.3.0

git clone https://github.com/GModal/vSwell
cd vSwell
git checkout $1
git submodule update --init --recursive
rm -rf .git dpf/.git
cd ..
tar cvfz vSwell.tar.gz vSwell/*
rm -rf vSwell
