#!/bin/bash

# ./chaffverb-source.sh <tag>
# ./chaffverb-source.sh v0.6.3

git clone https://github.com/GModal/ChaffVerb
cd ChaffVerb
git checkout $1
git submodule update --init --recursive
rm -rf .git dpf/.git
cd ..
tar cvfz ChaffVerb.tar.gz ChaffVerb/*
rm -rf ChaffVerb
