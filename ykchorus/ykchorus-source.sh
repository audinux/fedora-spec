#!/bin/bash

# ./ykchorus-source.sh <tag>
# ./ykchorus-source.sh v0.2.3

git clone https://github.com/SpotlightKid/ykchorus
cd ykchorus
git checkout $1
git submodule update --init --recursive
rm -rf .git dpf/.git
cd ..
tar cvfz ykchorus.tar.gz ykchorus/*
rm -rf ykchorus
