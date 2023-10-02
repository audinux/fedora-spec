#!/bin/bash

# Usage: ./guitarsynth-lv2-source.sh <TAG>
#        ./guitarsynth-lv2-source.sh master

git clone https://github.com/geraldmwangi/GuitarSynth-DPF
cd GuitarSynth-DPF
git checkout $1
git rm -f dpf
git submodule add https://github.com/DISTRHO/DPF dpf
cd dpf
git checkout 058388be8b2dc21d6da9cdd0b727571dba02290a
cd ..
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz GuitarSynth-DPF.tar.gz GuitarSynth-DPF/*
rm -rf GuitarSynth-DPF
