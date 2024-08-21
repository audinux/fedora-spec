#!/bin/bash

# ./qtractor-source.sh <tag>
# ./qtractor-source.sh qtractor_0_9_36

git clone https://github.com/rncbc/qtractor
cd qtractor
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz qtractor.tar.gz qtractor/
rm -rf qtractor
