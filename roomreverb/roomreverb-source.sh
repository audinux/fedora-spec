#!/bin/bash

# ./roomreverb-source.sh <tag>
# ./roomreverb-source.sh v0.6.1

git clone https://github.com/cvde/RoomReverb
cd RoomReverb
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz RoomReverb.tar.gz RoomReverb/*
rm -rf RoomReverb
