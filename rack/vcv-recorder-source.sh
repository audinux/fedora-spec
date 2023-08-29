#!/bin/bash

# ./vcv-recorder-source.sh <tag>
# ./vcv-recorder-source.sh v2

git clone https://github.com/VCVRack/VCV-Recorder
cd VCV-Recorder
git checkout $1
git submodule update --init --recursive --progress
find . -name ".git" -exec rm -rf {} \;
cd ..
tar cvfz VCV-Recorder.tar.gz VCV-Recorder
rm -rf VCV-Recorder
