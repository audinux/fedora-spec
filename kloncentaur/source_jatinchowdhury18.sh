#!/bin/bash

# Usage: ./source_jatinchowdhury18.sh <project> <tag>
#        ./source_jatinchowdhury18.sh AnalogTapeModel 1.2.0

git clone --recursive https://github.com/jatinchowdhury18/$1
cd $1
git checkout $2
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $2"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
