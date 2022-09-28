#!/bin/bash

# Usage: ./masterme-source.sh <TAG>
# ./masterme-source.sh 1.1.0

git clone https://github.com/trummerschlunk/master_me
cd master_me
git checkout $1
git submodule update --init --recursive
# Get the Faust sources
make faustpp/CMakeLists.txt
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz master_me.tar.gz master_me/*
rm -rf master_me

