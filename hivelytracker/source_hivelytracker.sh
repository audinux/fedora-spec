#!/bin/bash

# Usage: ./source_hivelytracker.sh <tag>
#        ./source_hivelytracker.sh master

git clone https://github.com/pete-gordon/hivelytracker
cd hivelytracker
git checkout $1
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz hivelytracker.tar.gz hivelytracker/*
rm -rf hivelytracker
