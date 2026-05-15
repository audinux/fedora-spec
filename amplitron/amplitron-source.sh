#!/bin/bash

# Usage: ./amplitron-source.sh <TAG>
#        ./amplitron-source.sh v0.1.71

git clone https://github.com/sudip-mondal-2002/Amplitron
cd Amplitron
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
git submodule update --depth=1 --init --recursive --progress
find . -name .git -exec rm -rf {} \;

# From .github/workflows/ci.yml
git clone --depth 1 --branch v1.90.1 https://github.com/ocornut/imgui.git external/imgui
curl -sL -o external/nanosvg.h https://raw.githubusercontent.com/memononen/nanosvg/master/src/nanosvg.h
curl -sL -o external/nanosvgrast.h https://raw.githubusercontent.com/memononen/nanosvg/master/src/nanosvgrast.h
curl -sL -o external/dr_wav.h https://raw.githubusercontent.com/mackron/dr_libs/master/dr_wav.h

mkdir -p external/kiss_fft
curl -sL -o external/kiss_fft/kiss_fft.h https://raw.githubusercontent.com/mborgerding/kissfft/master/kiss_fft.h
curl -sL -o external/kiss_fft/kiss_fft.c https://raw.githubusercontent.com/mborgerding/kissfft/master/kiss_fft.c
curl -sL -o external/kiss_fft/_kiss_fft_guts.h https://raw.githubusercontent.com/mborgerding/kissfft/master/_kiss_fft_guts.h
curl -sL -o external/kiss_fft/kiss_fft_log.h https://raw.githubusercontent.com/mborgerding/kissfft/master/kiss_fft_log.h

cd ..

tar cvfz Amplitron.tar.gz Amplitron/*
rm -rf Amplitron
