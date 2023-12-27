#!/bin/bash

# ./spotlightkid-source.sh <project> <tag>
# ./spotlightkid-source.sh stereocrossdelay master

git clone https://github.com/SpotlightKid/$1
cd $1
git checkout $2
git submodule update --init --recursive --verbose
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
