#!/bin/bash

RELEASE=44
REPOSITORY=audinux

dnf repoquery --releasever=$RELEASE --repoid=copr:copr.fedorainfracloud.org:ycollet:$REPOSITORY | grep src | sed -e "s/\.fc$RELEASE.src//g" | sort | uniq > packages-$RELEASE.txt
