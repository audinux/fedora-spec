#!/bin/bash

# To get adlplug source code: ./adlplug-source v1.0.2
git clone https://github.com/jpcima/ADLplug
cd ADLplug
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ADLplug.tar.gz ADLplug/*
rm -rf ADLplug
