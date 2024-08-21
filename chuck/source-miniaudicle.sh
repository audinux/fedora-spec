#!/bin/bash

# Usage: ./source-miniaudicle.sh <tag>
#        ./source-miniaudicle.sh miniAudicle-1.4.2.0

git clone https://github.com/ccrma/miniAudicle
cd miniAudicle
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz miniAudicle.tar.gz miniAudicle/*
rm -rf miniAudicle
