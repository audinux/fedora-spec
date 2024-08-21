#!/bin/bash

# to get source from 2.27.2 tag
# ./faust-source.sh 2.27.2

git clone https://github.com/grame-cncm/faust
cd faust
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz faust.tar.gz faust/*
rm -rf faust
