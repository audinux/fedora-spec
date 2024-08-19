#!/bin/bash

# ./source.sh 3.13

git clone https://github.com/zamaudio/zam-plugins
cd zam-plugins
git checkout $1
git submodule update --init --recursive --progress
make dist
mv *.tar.xz ..
cd ..
rm -rf zam-plugins
