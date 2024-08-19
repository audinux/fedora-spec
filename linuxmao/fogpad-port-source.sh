#!/bin/bash

# To get adlplug source code: ./fogpad-port-source v1.0.0
git clone https://github.com/linuxmao-org/fogpad-port
cd fogpad-port
git checkout $1
git submodule update --init --recursive --progresss
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz fogpad-port.tar.gz fogpad-port/*
rm -rf fogpad-port
