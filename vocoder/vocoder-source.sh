#!/bin/bash

# Usage: ./vocoder-sources.sh <TAG>
# ./vocoder-sources.sh main

git clone https://github.com/Stazed/vocoder
cd vocoder
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz vocoder.tar.gz vocoder/*
rm -rf vocoder
