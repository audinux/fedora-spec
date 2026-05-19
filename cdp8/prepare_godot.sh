#!/bin/bash

# Usage: ./prepare_godot.sh <VERSION>
#        ./prepare_godot.sh 4.6.2

VERSION=$1
wget https://godot-releases.nbg1.your-objectstorage.com/$VERSION-stable/Godot_v$VERSION-stable_export_templates.tpz
unzip Godot_v$VERSION-stable_export_templates.tpz

find templates -name "*.exe" -exec rm {} \;
find templates -name "*.zip" -exec rm {} \;
find templates -name "*.apk" -exec rm {} \;
find templates -name "*.arm32" -exec rm {} \;
find templates -name "*.x86_32" -exec rm {} \;
find templates -name "*_debug.*" -exec rm {} \;

cd templates/
zip -r godot_templates.zip *
mv godot_templates.zip ..
cd ..

rm -rf templates/
rm -f Godot_v$VERSION-stable_export_templates.tpz
