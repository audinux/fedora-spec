#!/bin/bash

# ./fil4-source.sh <tag>
# ./fil4-source.sh v0.4.4

git clone https://github.com/x42/fil4.lv2
cd fil4.lv2

# git protocol has been cancelled ...
git rm robtk
git commit -m "remove submodule"
git submodule add -b 1e82c83dc6655505d6be3f69af827787426df634 https://github.com/x42/robtk/
git add .gitmodules robtk
git commit -m "add submodule"
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz fil4.lv2.tar.gz fil4.lv2/*
rm -rf fil4.lv2
