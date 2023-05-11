#!/bin/bash

# ./x42-source.sh <project> <tag>
# ./x42-source.sh fil4.lv2 v0.4.4

git clone https://github.com/x42/$1
cd $1
git checkout $2

## git protocol has been cancelled ...
#if [ -d robtk ];
#then
#    COMMIT=`git submodule status | grep robtk | cut -d" " -f1 | sed -s "s/-//g"`
#    git rm robtk
#    git commit -m "remove submodule"
#    #git submodule add -b $COMMIT https://github.com/x42/robtk/ robtk
#    git submodule add https://github.com/x42/robtk/ robtk
#    git add .gitmodules robtk
#    git commit -m "add submodule"
#fi
git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz $1.tar.gz $1/*
rm -rf $1
