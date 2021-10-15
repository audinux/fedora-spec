#!/bin/bash

# ./xuidesigner-source.sh <tag>
# ./xuidesigner-source.sh v0.2

git clone https://github.com/brummer10/XUiDesigner
cd XUiDesigner
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz XUiDesigner.tar.gz XUiDesigner/*
rm -rf XUiDesigner
