#!/bin/bash

# Usage: ./ultramaster-kr106-source.sh <TAG>
#        ./ultramaster-kr106-source.sh v2.4.2

git clone https://github.com/kayrockscreenprinting/ultramaster_kr106
cd ultramaster_kr106
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ultramaster_kr106.tar.gz ultramaster_kr106/*
rm -rf ultramaster_kr106
