#!/bin/bash

# ./JDSP4Linux-source.sh <tag>
# ./JDSP4Linux-source.sh jamesdsp-2.3-1

git clone https://github.com/theAeon/JDSP4Linux
cd JDSP4Linux
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz JDSP4Linux.tar.gz JDSP4Linux
rm -rf JDSP4Linux
