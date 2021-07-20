#!/bin/bash

# ./element-source.sh <tag>
# ./element-source.sh 0.46.2

git clone https://github.com/kushview/Element
cd Element
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Element.tar.gz Element/*
rm -rf Element
