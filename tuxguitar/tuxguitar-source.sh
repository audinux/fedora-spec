#!/bin/bash

# Source file cleaned of potentially proprietary SF2, DLL, EXE files:
# Usage: ./tuxguitar-source.sh 1.5.6

export VERSION=$1
wget -N http://downloads.sourceforge.net/tuxguitar/tuxguitar-$VERSION-src.tar.gz
tar zxf tuxguitar-$VERSION-src.tar.gz
find tuxguitar-$VERSION-src -name "*.exe" -exec rm {} \;
find tuxguitar-$VERSION-src -name "*.dll" -exec rm {} \;
find tuxguitar-$VERSION-src -name "*.sf2" -exec rm {} \;
tar zcf tuxguitar-$VERSION-src-clean.tar.gz tuxguitar-$VERSION-src
