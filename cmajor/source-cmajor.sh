#!/bin/bash

# Usage: ./source-cmajor.sh <tag>
#        ./source-cmajor.sh 1.0.2562

git clone https://github.com/cmajor-lang/cmajor
cd cmajor
git checkout $1
git submodule update --init --recursive

git clone https://github.com/juce-framework/JUCE/ juce
cd juce
git checkout 7.0.12
cd ..

rm -rf 3rdParty/llvm/release/android
rm -rf 3rdParty/llvm/release/osx
rm -rf 3rdParty/llvm/release/wasm
rm -rf 3rdParty/llvm/release/win
rm -rf 3rdParty/llvm/release/win-static
rm -rf 3rdParty/llvm/release/linux/arm32

find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz cmajor.tar.gz cmajor/*
rm -rf cmajor
