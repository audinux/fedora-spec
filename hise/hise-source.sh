#!/bin/bash

# Usage: ./hise-source.sh <TAG>
#        ./hise-source.sh v4.9.3

git clone https://github.com/christophhart/HISE
cd HISE
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz HISE.tar.gz HISE/*
rm -rf HISE
