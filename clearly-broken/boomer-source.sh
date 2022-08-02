#!/bin/bash

# Usage: ./boomer-source.sh <TAG>
# ./boomer-source.sh 1916d46a2823d0f091edf545666058456c93b004

git clone https://github.com/clearly-broken-software/boomer/
cd boomer
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz boomer.tar.gz boomer/*
rm -rf boomer
