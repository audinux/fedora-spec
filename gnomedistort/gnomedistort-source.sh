#!/bin/bash

# Usage: ./gnomedistort-source.sh <TAG>
#        ./gnomedistort-source.sh v1.0.0

git clone https://github.com/crowbait/GnomeDistort-2
cd GnomeDistort-2
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz GnomeDistort-2.tar.gz GnomeDistort-2/*
rm -rf GnomeDistort-2
