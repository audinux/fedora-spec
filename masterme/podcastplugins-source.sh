#!/bin/bash

# Usage: ./podcastplugins-source.sh <TAG>
#        ./podcastplugins-source.sh 1.0.0

git clone https://github.com/trummerschlunk/PodcastPlugins
cd PodcastPlugins
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
# Get the Faust sources
make faustpp/CMakeLists.txt
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz PodcastPlugins.tar.gz PodcastPlugins/*
rm -rf PodcastPlugins

