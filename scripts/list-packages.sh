#!/bin/bash

RELEASE=35
REPOSITORY=audinux

dnf repoquery --release=$RELEASE --repoid=copr:copr.fedorainfracloud.org:ycollet:$REPOSITORY | grep src | sed -e "s/\.fc$RELEASE.src//g" | sort | uniq > packages-$RELEASE.txt
