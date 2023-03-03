#!/bin/bash

# Usage: ./grandorgue-sources.sh <TAG>
# ./grandorgue-sources.sh v2.3.4

git clone https://github.com/GrandOrgue/grandorgue
cd grandorgue
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz grandorgue.tar.gz grandorgue/*
rm -rf grandorgue
