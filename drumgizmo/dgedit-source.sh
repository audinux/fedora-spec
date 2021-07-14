#!/bin/bash

# To get dgedit source code: ./dgedit-source.sh v0.10.0
git clone http://git.drumgizmo.org/dgedit.git
cd dgedit
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz dgedit.tar.gz dgedit/*
rm -rf dgedit
