#!/bin/bash

# ./fugio-source.sh <tag>
# ./fugio-source.sh v3.1.0

git clone https://github.com/bigfug/Fugio
cd Fugio
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Fugio.tar.gz Fugio/*
rm -rf Fugio
