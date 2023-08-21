#!/bin/bash

# To get RCVerb source code:
# ./rcverb-source.sh v1.0
git clone https://github.com/chmaha/RCVerb
cd RCVerb
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz RCVerb.tar.gz RCVerb/*
rm -rf RCVerb
