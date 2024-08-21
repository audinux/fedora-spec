#!/bin/bash

# Usage: ./airwin2rack-source.sh <TAG>
#        ./airwin2rack-source.sh master

git clone https://github.com/baconpaul/airwin2rack
cd airwin2rack
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz airwin2rack.tar.gz airwin2rack/*
rm -rf airwin2rack
