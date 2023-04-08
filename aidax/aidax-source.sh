#!/bin/bash

# To get aidax source code:
# $ ./aidax-source.sh 0.1.0

git clone https://github.com/AidaDSP/AIDA-X
cd AIDA-X
git checkout $1
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz AIDA-X.tar.gz AIDA-X/*
rm -rf AIDA-X
