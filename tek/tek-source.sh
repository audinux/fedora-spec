#!/bin/bash

# Usage: ./tek-source.sh <TAG>
#        ./tek-source.sh 0.2.2

git clone https://codeberg.org/unspeaker/tek/
cd tek
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz tek.tar.gz tek/*
rm -rf tek
