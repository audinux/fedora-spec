#!/bin/bash

# ./check_all_packages_are_built.sh [release]
LIST=`find .. -name "*.spec" | sort | uniq`
FN='missing_packages.txt'
RELEASE=43
if [[ $# -eq 1 ]]; then
    RELEASE=$1
fi

echo "Updating database for F$RELEASE"
dnf --releasever=$RELEASE --refresh search emacs 2>&1 > /dev/null

echo "" > $FN
for Files in $LIST
do
    NAME=`grep "Name:" $Files | sed -e "s/Name:[ ]*//g"`
    STATUS=`grep "# Status:" $Files | sed -e "s/# Status:[ ]*//g"`

    echo "Processing spec file $Files for package name $NAME (status: $STATUS)"

    RESULT=`LANG=C dnf --releasever=$RELEASE search $NAME 2>&1`
    RESULT=`echo $RESULT | grep "No matches found"`
    if [ ! -z "$RESULT" ]; then
	echo "Package $NAME is missing"
	echo "Package $NAME from file $Files is missing (status: $STATUS)" >> $FN
    fi
done
