#!/bin/bash

# ./xtuner-source.sh <tag>
# ./xtuner-source.sh v1.0

git clone https://github.com/brummer10/XTuner
cd XTuner
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz XTuner.tar.gz XTuner/*
rm -rf XTuner
