#!/bin/bash

# Usage: ./source-sickbeatbetty.sh <tag>
#        ./source-sickbeatbetty.sh v1.0.3

git clone https://github.com/jthwho/SickBeatBetty
cd SickBeatBetty
git checkout $1
git submodule init
git submodule update
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz SickBeatBetty.tar.gz SickBeatBetty/*
rm -rf SickBeatBetty
