#!/bin/bash

# Usage: ./source-shortcircuit.sh <tag>
#        ./source-shortcircuit.sh main

git clone https://github.com/surge-synthesizer/shortcircuit-xt
cd shortcircuit-xt
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
# find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz shortcircuit-xt.tar.gz shortcircuit-xt
rm -rf shortcircuit-xt
