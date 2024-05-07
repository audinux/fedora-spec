#!/bin/bash

# Usage: ./airwin2rack-source.sh <TAG>
#        ./airwin2rack-source.sh master

git clone https://github.com/baconpaul/airwin2rack
cd airwin2rack
git checkout $1
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz airwin2rack.tar.gz airwin2rack/*
rm -rf airwin2rack
