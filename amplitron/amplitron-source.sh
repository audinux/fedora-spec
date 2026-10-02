#!/bin/bash

# Usage: ./amplitron-source.sh <TAG>
#        ./amplitron-source.sh v0.1.71

git clone https://github.com/sudip-mondal-2002/Amplitron
cd Amplitron
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
if [ $? -ne 0 ]; then
    echo "Problem with submodules"
    exit 1
fi

./scripts/setup_dependencies.sh

find . -name .git -exec rm -rf {} \;

cd ..

tar cvfz Amplitron.tar.gz Amplitron/*
rm -rf Amplitron
