#!/bin/bash

# ./opn2bankeditor-source.sh <tag>
# ./opn2bankeditor-source.sh v1.3

git clone https://github.com/Wohlstand/OPN2BankEditor
cd OPN2BankEditor
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz OPN2BankEditor.tar.gz OPN2BankEditor/*
rm -rf OPN2BankEditor
