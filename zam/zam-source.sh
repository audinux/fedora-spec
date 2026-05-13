#!/bin/bash

# ./source.sh 3.13

git clone --depth=1 https://github.com/zamaudio/zam-plugins
cd zam-plugins
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
make dist
mv *.tar.xz ..
cd ..
rm -rf zam-plugins
