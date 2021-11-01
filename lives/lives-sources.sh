#!/bin/bash

# Usage: ./lives-source.sh <TAG>
# ./lives-source.sh master

git clone https://github.com/salsaman/LiVES
cd LiVES
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz LiVES.tar.gz LiVES/*
rm -rf LiVES

