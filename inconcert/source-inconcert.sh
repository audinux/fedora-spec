#!/bin/bash

# Usage: ./source-inconcert.sh <tag>
#        ./source-inconcert.sh 5362b3419c924051c599764c4885ce0db0264091

git clone git://gabe.is-a-geek.org/git/inconcert.git
cd inconcert
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz inconcert.tar.gz inconcert/*
rm -rf inconcert
