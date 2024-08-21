#!/bin/bash

# Usage:
# ./aether-source <TAG>
# ./aether-source v1.2.1

git clone https://github.com/Dougal-s/Aether
cd Aether
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Aether.tar.gz Aether/*
rm -rf Aether
