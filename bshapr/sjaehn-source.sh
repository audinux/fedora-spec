#!/bin/bash

# ./sjaehn-source.sh <project> <tag>
# ./sjaehn-source.sh BChoppr 1.12.4

git clone https://github.com/sjaehn/$1
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
