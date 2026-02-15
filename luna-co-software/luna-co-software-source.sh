#!/bin/bash

# Usage: ./luna-co-software-source.sh <TAG>
#        ./luna-co-software-source.sh main

git clone https://github.com/dusk-audio/dusk-audio-plugins
cd dusk-audio-plugins
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
git submodule add https://github.com/juce-framework/JUCE.git external/JUCE

find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz dusk-audio-plugins.tar.gz dusk-audio-plugins/*
rm -rf dusk-audio-plugins
