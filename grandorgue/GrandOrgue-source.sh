#!/bin/bash

# Usage: ./grandorgue-sources.sh <TAG>
# ./grandorgue-sources.sh v2.3.4

git clone https://github.com/GrandOrgue/grandorgue
cd grandorgue
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz grandorgue.tar.gz grandorgue/*
rm -rf grandorgue
