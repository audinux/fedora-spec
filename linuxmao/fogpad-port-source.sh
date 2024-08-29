#!/bin/bash

# To get source code: ./fogpad-port-source.sh v1.0.0
git clone https://github.com/linuxmao-org/fogpad-port
cd fogpad-port
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz fogpad-port.tar.gz fogpad-port/*
rm -rf fogpad-port
