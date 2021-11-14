#!/bin/bash

# ./xuidesigner-source.sh <tag>
# ./xuidesigner-source.sh v0.3

git clone -b $1 --recursive https://github.com/brummer10/XUiDesigner
cd XUiDesigner
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz XUiDesigner.tar.gz XUiDesigner/*
rm -rf XUiDesigner
