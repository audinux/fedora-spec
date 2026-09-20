#!/bin/bash

# Usage: ./ssr-source.sh <TAG>
#        ./ssr-source.sh master

git clone https://github.com/SoundScapeRenderer/ssr/
cd ssr
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ssr.tar.gz ssr/*
rm -rf ssr
