#!/bin/bash

RELEASE=37
REPOSITORY=audinux

dnf repoquery --release=$RELEASE --repoid=copr:copr.fedorainfracloud.org:ycollet:$REPOSITORY | grep src | sed -e "s/\.fc$RELEASE.src//g" | sort | uniq > packages-$RELEASE.txt
