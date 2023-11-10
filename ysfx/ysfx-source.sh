#!/bin/bash

# To get adlplug source code: ./ysfx-source master
git clone https://github.com/jpcima/ysfx
cd ysfx
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ysfx.tar.gz ysfx/*
rm -rf ysfx
