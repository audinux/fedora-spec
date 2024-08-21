#!/bin/bash

# Usage: ./source-midi-monitor.sh <tag>
#        ./source-midi-monitor.sh main

git clone https://github.com/surge-synthesizer/midi-monitor
cd midi-monitor
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz midi-monitor.tar.gz midi-monitor/*
rm -rf midi-monitor
