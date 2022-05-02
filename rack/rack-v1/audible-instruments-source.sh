#!/bin/bash

# ./audible-instruments-source.sh <tag>
# ./audible-instruments-source.sh v1.4.0

git clone https://github.com/VCVRack/AudibleInstruments.git
cd AudibleInstruments
git checkout $1
git submodule update --init --recursive
find . -name ".git" -exec rm -rf {} \;
cd ..
tar cvfz AudibleInstruments.tar.gz AudibleInstruments
rm -rf AudibleInstruments
