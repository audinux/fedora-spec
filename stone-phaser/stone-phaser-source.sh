#!/bin/bash

# ./stone-phaser-source.sh <tag>
# ./stone-phaser-source.sh v0.1.2

git clone https://github.com/jpcima/stone-phaser
cd stone-phaser
# git protocol has been cancelled ...
git submodule set-url -- dpf https://github.com/DISTRHO/DPF
git add .gitmodules
git commit -m "update module"
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz stone-phaser.tar.gz stone-phaser/*
rm -rf stone-phaser
