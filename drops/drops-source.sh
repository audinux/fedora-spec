#!/bin/bash

# Usage: ./drops-source.sh <TAG>
#        ./drops-source.sh v1.0-beta2

git clone https://github.com/clearly-broken-software/drops
cd drops
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz drops.tar.gz drops/*
rm -rf drops

