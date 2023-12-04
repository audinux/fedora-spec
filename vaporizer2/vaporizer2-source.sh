#!/bin/bash

# Usage: ./vaporizer2-source.sh <tag>
#        ./vaporizer2-source.sh v3.4.0

git clone https://github.com/VASTDynamics/Vaporizer2
cd Vaporizer2
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Vaporizer2.tar.gz Vaporizer2/*
rm -rf Vaporizer2
