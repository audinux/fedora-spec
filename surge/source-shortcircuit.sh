#!/bin/bash

# Usage: ./source-shortcircuit.sh <tag>
#        ./source-shortcircuit.sh main

git clone https://github.com/surge-synthesizer/shortcircuit3
cd shortcircuit3
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz shortcircuit.tar.gz shortcircuit3/*
rm -rf shortcircuit3
