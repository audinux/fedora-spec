#!/bin/bash

# Usage: ./sfizz-ui-source.sh <tag>
#        ./sfizz-ui-source.sh 1.2.2

git clone https://github.com/sfztools/sfizz-ui
cd sfizz-ui
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz sfizz-ui.tar.gz sfizz-ui/*
rm -rf sfizz-ui
