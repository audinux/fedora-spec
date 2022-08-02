#!/bin/bash

# Usage: ./punch-source.sh <TAG>
# ./punch-source.sh 3969dc2fda5afe856a2a515de5c14b345f6891d1

git clone https://github.com/clearly-broken-software/Punch/
cd Punch
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz Punch.tar.gz Punch/*
rm -rf Punch
