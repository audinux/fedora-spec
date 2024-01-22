#!/bin/bash

# ./clap-source.sh <project> <tag>
# ./clap-source.sh clap-plugins 1.0.1

git clone https://github.com/free-audio/$1
cd $1
git checkout $2
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
