#!/bin/bash

# Usage: ./element-source.sh <TAG>
#        ./element-source.sh v1.0.0b2

git clone https://github.com/kushview/Element/
cd Element
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Element.tar.gz Element/*
rm -rf Element
