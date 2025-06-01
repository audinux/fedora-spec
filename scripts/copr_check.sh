#!/bin/bash

wget -q --spider https://google.com

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

dnf repoquery --repoid=copr:copr.fedorainfracloud.org:ycollet:audinux --queryformat "%{full_nevra} %{buildtime}\n" | sort -k2 | sed -e "s/^[ ]*//g" | sed -e "s/ /__/g" > copr_tags_new.txt

if [ -f copr_tags_old.txt ];
then
    echo -e "\n\n\n"
    echo "==================="
    echo "= Changes in COPR ="
    echo "===================" 
    echo -e "\n\n\n"

    diff copr_tags_new.txt copr_tags_old.txt
fi

