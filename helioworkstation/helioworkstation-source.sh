#!/bin/bash

# ./source.sh tag -> ./source.sh 3.6

git clone https://github.com/helio-fm/helio-workstation
cd helio-workstation
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz helio-workstation.tar.gz helio-workstation/
rm -rf helio-workstation
