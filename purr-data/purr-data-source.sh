#!/bin/bash

# ./purr-data-source.sh <tag>
# ./purr-data-source.sh 2.17.0

git clone https://github.com/agraef/purr-data
cd purr-data
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz purr-data.tar.gz purr-data
rm -rf purr-data
