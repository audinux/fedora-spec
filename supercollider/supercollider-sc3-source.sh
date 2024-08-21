#!/bin/bash

# ./supercollider-sc3-source.sh <tag>
# ./supercollider-sc3-source.sh Version-3.11.1

git clone https://github.com/supercollider/sc3-plugins
cd sc3-plugins
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz sc3-plugins.tar.gz sc3-plugins
rm -rf sc3-plugins
