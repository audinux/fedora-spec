#!/bin/bash

git clone --depth=1 https://github.com/falkTX/non non-daw-lv2
cd non-daw-lv2
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz non-daw-lv2.tar.gz non-daw-lv2/*
rm -rf non-daw-lv2
