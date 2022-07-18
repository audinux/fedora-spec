#!/bin/bash

# ./roomreverb-source.sh <tag>
# ./roomreverb-source.sh v0.6.1

git clone -b $1 --recursive https://github.com/cvde/RoomReverb
cd RoomReverb
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz RoomReverb.tar.gz RoomReverb/*
rm -rf RoomReverb
