#!/bin/bash

# Usage: ./jack-link-source.sh <TAG>
#        ./jack-link-source.sh v0.1.8

git clone https://github.com/rncbc/jack_link
cd jack_link
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz jack_link.tar.gz jack_link/*
rm -rf jack_link
