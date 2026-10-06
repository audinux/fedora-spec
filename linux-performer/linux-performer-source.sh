#!/bin/bash

# Usage: ./linux-performer-source.sh <TAG>
#        ./linux-performer-source.sh v0.1.41

git clone https://github.com/dguedry/linux-performer/
cd linux-performer
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
if [ $? -ne 0 ]; then
    echo "Problem with submodules"
    exit 1
fi
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz linux-performer.tar.gz linux-performer/*
rm -rf linux-performer
