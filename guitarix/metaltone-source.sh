#!/bin/bash

git clone https://github.com/brummer10/MetalTone
cd MetalTone
git switch $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz MetalTone.tar.gz MetalTone/*
rm -rf MetalTone
