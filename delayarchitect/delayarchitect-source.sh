#!/bin/bash

# ./delayarchitect-source.sh <tag>
# ./delayarchitect-source.sh master

git clone https://github.com/jpcima/DelayArchitect
cd DelayArchitect
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz DelayArchitect.tar.gz DelayArchitect/*
rm -rf DelayArchitect
