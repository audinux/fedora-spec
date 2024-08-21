#!/bin/bash

# Usage: ./gnomedistort-source.sh <TAG>
#        ./gnomedistort-source.sh v1.0.0

git clone https://github.com/crowbait/GnomeDistort-2
cd GnomeDistort-2
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz GnomeDistort-2.tar.gz GnomeDistort-2/*
rm -rf GnomeDistort-2
