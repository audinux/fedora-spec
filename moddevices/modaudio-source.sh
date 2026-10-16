#!/bin/bash

# ./modaudio-source.sh <project> <tag>
# ./modaudio-source.sh mod-midi-merger 2209dbf6259c414384bcdefd7929bab77926d8eb

git clone https://github.com/mod-audio/$1
cd $1
git checkout $2
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $2"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
if [ $? -ne 0 ]; then
    echo "Problem with submodules"
    exit 1
fi
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
md5sum $1.tar.gz
