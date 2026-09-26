#!/bin/bash

git clone https://github.com/falkTX/non non-daw-lv2
cd non-daw-lv2
git submodule update --depth=1 --init --recursive --progress
if [ $? -ne 0 ]; then
    echo "Problem with submodules"
    exit 1
fi
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz non-daw-lv2.tar.gz non-daw-lv2/*
rm -rf non-daw-lv2
