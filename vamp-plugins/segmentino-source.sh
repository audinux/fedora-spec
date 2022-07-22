#!/bin/bash

wget https://code.soundsoftware.ac.uk/attachments/download/2458/segmentino-v1.1.tar.gz
tar xvfz segmentino-v1.1.tar.gz
cd segmentino-v1.1
./repoint install
sed -i -e "s/.repoint.point //g" Makefile.inc
cd ..
rm segmentino-v1.1.tar.gz
tar cvfz segmentino-v1.1.tar.gz segmentino-v1.1/
rm -rf segmentino-v1.1/
