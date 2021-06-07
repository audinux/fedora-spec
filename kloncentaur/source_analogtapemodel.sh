#!/bin/bash

# Usage: ./source_analogtapemodel.sh <tag>
#        ./source_analogtapemodel.sh 1.2.0

git clone --recursive https://github.com/jatinchowdhury18/AnalogTapeModel
cd AnalogTapeModel
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz AnalogTapeModel.tar.gz AnalogTapeModel/*
rm -rf AnalogTapeModel
