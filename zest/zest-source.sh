#!/bin/bash

# Usage: ./zest-source.sh <TAG>
#        ./zest-source.sh 3.0.6

git clone https://github.com/mruby-zest/mruby-zest-build
cd mruby-zest-build
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi

# initialize submodules
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz mruby-zest-build.tar.gz mruby-zest-build/*
rm -rf mruby-zest-build
