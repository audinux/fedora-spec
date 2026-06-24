#!/bin/bash

# Usage: ./nextstudio-source.sh <TAG>
#        ./nextstudio-source.sh v0.02-alpha

git clone https://github.com/BaraMGB/NextStudio
cd NextStudio
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz NextStudio.tar.gz NextStudio/*
rm -rf NextStudio
