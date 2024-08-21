#!/bin/bash

# ./opl3bankeditor-source.sh <tag>
# ./opl3bankeditor-source.sh v1.5.1

git clone https://github.com/Wohlstand/OPL3BankEditor
cd OPL3BankEditor
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz OPL3BankEditor.tar.gz OPL3BankEditor/*
rm -rf OPL3BankEditor
