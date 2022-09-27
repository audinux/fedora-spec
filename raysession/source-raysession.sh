#!/bin/bash

# Usage: ./source-raysession.sh <tag>
#        ./source-raysession.sh v0.13.0

git clone https://github.com/Houston4444/RaySession
cd RaySession
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz RaySession.tar.gz RaySession/*
rm -rf RaySession
