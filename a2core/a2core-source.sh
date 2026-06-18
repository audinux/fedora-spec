#!/bin/bash

# Usage: ./a2core-source.sh <TAG>
#        ./a2core-source.sh main

git clone https://codeberg.org/yimrakhee/a2core.lv2
cd a2core.lv2
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz a2core.lv2.tar.gz a2core.lv2/*
rm -rf a2core.lv2
