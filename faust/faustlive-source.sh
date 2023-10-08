#!/bin/bash

# to get source!
# ./faustlive-source.sh 2.5.15

git clone https://github.com/grame-cncm/faustlive
cd faustlive
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz faustlive.tar.gz faustlive/*
rm -rf faustlive
