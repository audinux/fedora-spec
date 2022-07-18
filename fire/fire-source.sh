#!/bin/bash

# Usage: ./fire-sources.sh <TAG>
# ./fire-sources.sh v0.9.8

git clone https://github.com/jerryuhoo/Fire/
cd Fire
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Fire.tar.gz Fire/*
rm -rf Fire
