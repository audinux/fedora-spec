#!/bin/bash

# Usage: ./drummock-source.sh <TAG>
#        ./drummock-source.sh 0.0.1

git clone https://github.com/ameyakakade/drummock/
cd drummock
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz drummock.tar.gz drummock/*
rm -rf drummock
