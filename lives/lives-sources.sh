#!/bin/bash

# Usage: ./lives-sources.sh <TAG>
# ./lives-sources.sh master

git clone --recursive https://github.com/salsaman/LiVES
cd LiVES
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz LiVES.tar.gz LiVES/*
rm -rf LiVES

