#!/bin/bash

# Usage: ./stretcher-source.sh <TAG>
# ./stretcher-source.sh c7dc69b207e0fc44789450f1d2d121b9a887ddf1

git clone https://github.com/clearly-broken-software/Stretcher/
cd Stretcher
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Stretcher.tar.gz Stretcher/*
rm -rf Stretcher
