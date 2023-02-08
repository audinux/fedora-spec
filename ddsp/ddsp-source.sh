#!/bin/bash

# Usage: ./ddps-source.sh <TAG>
# ./ddsp-source.sh v1.1.0

git clone https://github.com/tank-trax/ddsp-vst
cd ddsp-vst
git switch linux
git checkout $1
git submodule update --init --recursive
./repo-init.sh
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz ddsp-vst.tar.gz ddsp-vst/*
rm -rf ddsp-vst
