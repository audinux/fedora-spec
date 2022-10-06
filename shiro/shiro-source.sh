#!/bin/bash

# ./shiro-source.sh <tag>
# ./shiro-source.sh master

git clone https://github.com/ninodewit/SHIRO-Plugins
cd SHIRO-Plugins
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz SHIRO-Plugins.tar.gz SHIRO-Plugins/*
rm -rf SHIRO-Plugins
