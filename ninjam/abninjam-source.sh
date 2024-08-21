#!/bin/bash

# ./abninjam-source.sh <tag>
# ./abninjam-source.sh v0.0.8

git clone https://github.com/antanasbruzas/abNinjam
cd abNinjam
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz abNinjam.tar.gz abNinjam/*
rm -rf abNinjam
