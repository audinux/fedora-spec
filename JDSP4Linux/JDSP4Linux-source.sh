#!/bin/bash

# ./JDSP4Linux-source.sh <tag>
# ./JDSP4Linux-source.sh jamesdsp-2.3-1

git clone https://github.com/theAeon/JDSP4Linux
cd JDSP4Linux
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz JDSP4Linux.tar.gz JDSP4Linux
rm -rf JDSP4Linux
