#!/bin/bash

# Usage: ./formula-source.sh <TAG>
#        ./formula-source.sh v1.2.2

git clone https://github.com/soundspear/formula
cd formula
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;

echo "Installing JUCE"
JuceVersion="8.0.4"
if [[ ! -d "JUCE" ]]; then
  curl -s -L "https://github.com/juce-framework/JUCE/archive/refs/tags/$JuceVersion.tar.gz" | tar xvz -C .
  mv JUCE-$JuceVersion JUCE
  chmod -R 777 JUCE
fi

cd ..
tar cvfz formula.tar.gz formula/*
rm -rf formula
