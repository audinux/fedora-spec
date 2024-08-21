#!/bin/bash

# Usage: ./ddps-source.sh <TAG>
# ./ddsp-source.sh v1.1.0

git clone https://github.com/tank-trax/ddsp-vst
cd ddsp-vst
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
./repo-init.sh
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ddsp-vst.tar.gz ddsp-vst/*
rm -rf ddsp-vst
