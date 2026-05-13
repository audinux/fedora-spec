#!/bin/bash

# Usage: ./neural-amp-modeler-lv2-source.sh <TAG>
# ./neural-amp-modeler-lv2-source.sh master

git clone --depth=1 https://github.com/mikeoliphant/neural-amp-modeler-lv2
cd neural-amp-modeler-lv2
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz neural-amp-modeler-lv2.tar.gz neural-amp-modeler-lv2/*
rm -rf neural-amp-modeler-lv2
