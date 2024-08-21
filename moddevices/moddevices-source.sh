#!/bin/bash

# ./moddevices-source.sh <project> <tag>
# ./moddevices-source.sh mod-cv-plugins 5b175482a32094f39eb46d569ffbc718b157a0ee

git clone https://github.com/moddevices/$1
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
