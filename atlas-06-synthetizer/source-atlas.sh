#!/bin/bash

# Usage: ./source-atlas.sh <tag>
#        ./source-atlas.sh master

git clone https://github.com/sbadon122/ATLAS-06-Synthesizer
cd ATLAS-06-Synthesizer
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ATLAS-06-Synthesizer.tar.gz ATLAS-06-Synthesizer/*
rm -rf ATLAS-06-Synthesizer
