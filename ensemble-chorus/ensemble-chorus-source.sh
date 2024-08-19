#!/bin/bash

# To get ensemble-chorus source code: ./ensemble-choris-source master
git clone https://github.com/jpcima/ensemble-chorus
cd ensemble-chorus
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ensemble-chorus.tar.gz ensemble-chorus/*
rm -rf ensemble-chorus
