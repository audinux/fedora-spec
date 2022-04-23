#!/bin/bash

git clone https://github.com/brummer10/CollisionDrive
cd CollisionDrive
git switch $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz CollisionDrive.tar.gz CollisionDrive/*
rm -rf CollisionDrive
