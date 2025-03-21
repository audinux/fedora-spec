#!/bin/bash

# Usage: ./source_hivelytracker.sh <tag>
#        ./source_hivelytracker.sh master

git clone https://github.com/pete-gordon/hivelytracker
cd hivelytracker
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz hivelytracker.tar.gz hivelytracker/*
rm -rf hivelytracker
