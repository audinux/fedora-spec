#!/bin/bash

# ./ossia-source.sh <tag>
# ./ossia-source.sh v3.0.1

git clone https://github.com/OSSIA/score
cd score
git checkout $1
git submodule init
git submodule update --recursive

cd 3rdparty/
LIBS=`ls -d */`
for Lib in $LIBS
do
    cd $Lib
    git submodule init
    git submodule update --recursive
    cd ..
done
cd ..

cd 3rdparty/libossia/3rdparty
LIBS=`ls -d */`
for Lib in $LIBS
do
    cd $Lib
    git submodule init
    git submodule update --recursive
    cd ..
done
cd ../..

cd snappy
LIBS=`ls -d */`
for Lib in $LIBS
do
    cd $Lib
    git submodule init
    git submodule update --recursive
    cd ..
done
cd ..

cd libpd
LIBS=`ls -d */`
for Lib in $LIBS
do
    cd $Lib
    git submodule init
    git submodule update --recursive
    cd ..
done
cd ../..

find . -name .git -exec rm -rf {} \;
cd ..
mv score score-$1
tar cvfz score-$1.tar.gz score-$1/*
rm -rf score-$1
