#!/bin/bash

# Usage: ./solfege-source.sh <TAG>
#        ./solfege-source.sh 3.23.5pre2

git clone --depth=1 https://git.savannah.gnu.org/git/solfege.git
cd solfege
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz solfege.tar.gz solfege/*
rm -rf solfege
