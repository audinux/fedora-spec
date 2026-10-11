#!/bin/bash

PACKAGES_LIST=`dnf repoquery --repoid=copr:copr.fedorainfracloud.org:ycollet:audinux --queryformat "%{full_nevra} %{buildtime}\n" | sort -k2 | sed -e "s/^[ ]*//g" | sed -e "s/ /__/g"`

for Files in $PACKAGES_LIST
do
    PACKAGE=`echo $Files | sed -e "s/^\(.*\)__\(.*\)$/\1/g"`
    DATE=`echo $Files | sed -e "s/^\(.*\)__\(.*\)$/\2/g"`
    DATE=`date -ud "@$DATE"`
    echo "$PACKAGE - $DATE"
done
