#!/bin/bash

RELEASEVER=`cat /etc/fedora-release | cut -d' ' -f3`
RELEASEVER=39
TMPDIR="tmp"

mkdir -p $TMPDIR
cd $TMPDIR

for Files in `dnf --releasever $RELEASEVER list --available | grep ycollet | grep src | cut -d" " -f1 | sed -e "s/\.src//g"`
do
    echo "Downloading $Files SRPMS file"
    dnf --releasever $RELEASEVER download --source $Files > /dev/null
done

cd ..
