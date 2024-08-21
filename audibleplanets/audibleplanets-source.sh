#!/bin/bash

# Usage: ./audibleplanets-sources.sh <TAG>
#        ./audibleplanets-sources.sh v1.0.4

git clone https://github.com/gregrecco67/AudiblePlanets
cd AudiblePlanets
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz AudiblePlanets.tar.gz AudiblePlanets/*
rm -rf AudiblePlanets
