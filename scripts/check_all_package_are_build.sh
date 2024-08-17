#!/bin/bash

LIST=`find .. -name "*.spec" -exec grep "Name:" {} \; | sed -e "s/Name:[ ]*//g" | sort | uniq`

for Files in $LIST
do
    echo "Processing spec for $Files"
    RESULT=`LANG=C dnf search $Files 2>&1 > /dev/null`
    RESULT=`echo $RESULT | grep "No matches found"`
    if [ ! -z "$RESULT" ]; then
       echo "Package $Files is missing"
    fi
done
