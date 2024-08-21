#!/bin/bash

# ./source_openframeworks.sh 0.11.2

# original tarfile can be found here:
git clone https://github.com/openframeworks/openFrameworks
cd openFrameworks
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
./scripts/linux/download_libs.sh
find . -name .git -exec rm -rf {} \;
cd ..
tar cvf openFrameworks.tar.gz openFrameworks/*
rm -rf openFrameworks
