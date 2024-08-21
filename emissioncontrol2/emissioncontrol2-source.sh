#!/bin/bash

# Usage: ./emissioncontrol2-source.sh <TAG>
#        ./emissioncontrol2-source.sh v1.2

git clone https://github.com/EmissionControl2/EmissionControl2
cd EmissionControl2
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz EmissionControl2.tar.gz EmissionControl2/*
rm -rf EmissionControl2
