#!/bin/bash

# ./chaffverb-source.sh <tag>
# ./chaffverb-source.sh v0.6.3

git clone https://github.com/GModal/ChaffVerb
cd ChaffVerb
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
rm -rf .git dpf/.git
cd ..
tar cvfz ChaffVerb.tar.gz ChaffVerb/*
rm -rf ChaffVerb
