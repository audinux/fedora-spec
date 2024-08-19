#!/bin/bash

# Usage: ./source-sickbeatbetty.sh <tag>
#        ./source-sickbeatbetty.sh v1.0.3

git clone https://github.com/jthwho/SickBeatBetty
cd SickBeatBetty
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz SickBeatBetty.tar.gz SickBeatBetty/*
rm -rf SickBeatBetty
