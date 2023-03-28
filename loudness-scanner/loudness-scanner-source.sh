#/bin/bash

# ./loudness-scanner-source.sh <tag>
# ./loudness-scanner-source.sh v0.5.1

git clone https://github.com/jiixyj/loudness-scanner
cd loudness-scanner
git checkout $1

# git protocol has been cancelled ...
if [ -d ebur128 ];
then
    COMMIT=`git submodule status | grep ebur128 | cut -d" " -f1 | sed -s "s/-//g"`
    git rm ebur128
    git commit -m "remove submodule"
    git submodule add https://github.com/jiixyj/libebur128 ebur128
    git add .gitmodules ebur128
    git commit -m "add submodule"
fi

if [ -d scanner/filetree ];
then
    COMMIT=`git submodule status | grep filetree | cut -d" " -f1 | sed -s "s/-//g"`
    git rm scanner/filetree
    git commit -m "remove submodule"
    git submodule add https://github.com/jiixyj/filewalk/ scanner/filetree
    git add .gitmodules scanner/filetree
    git commit -m "add submodule"
fi

git submodule update --init --recursive
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz loudness-scanner.tar.gz loudness-scanner/*
rm -rf loudness-scanner
