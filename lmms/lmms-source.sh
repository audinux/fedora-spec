#!/bin/bash

# ./lmms-source.sh <tag>
# ./lmms-source.sh v1.2.2

git clone https://github.com/lmms/lmms
cd lmms
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz lmms.tar.gz lmms/
rm -rf lmms
