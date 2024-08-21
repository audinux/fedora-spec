#!/bin/bash

# ./delayarchitect-source.sh <tag>
# ./delayarchitect-source.sh master

git clone https://github.com/jpcima/DelayArchitect
cd DelayArchitect
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz DelayArchitect.tar.gz DelayArchitect/*
rm -rf DelayArchitect
