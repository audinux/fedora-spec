#!/bin/bash

# ./midilooper-source.sh <tag>
# ./midilooper-source.sh 0.0.2.1

git clone https://github.com/supergilbert/midilooper
cd midilooper
git checkout $1
git submodule update --init --recursive --progress
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz midilooper.tar.gz midilooper/
rm -rf midilooper
