#!/bin/bash

wget -q --spider http://google.com

if [ $? -eq 0 ]; then
    echo "Net connection OK"
else
    echo "No net connection"
    exit
fi

if [ -f copr_tags_new.txt ];
then
    mv copr_tags_new.txt copr_tags_old.txt
fi

dnf repoquery --repoid=copr:copr.fedorainfracloud.org:ycollet:audinux --queryformat "%45{name} %{evr} %{buildtime}" | sort -r -k3 > copr_tags_new.txt

if [ -f copr_tags_old.txt ];
then
    echo -e "\n\n\n"
    echo "==================="
    echo "= Changes in COPR ="
    echo "===================" 
    echo -e "\n\n\n"

    diff copr_tags_new.txt copr_tags_old.txt
fi

