#!/bin/bash

RELEASE=35
REPOSITORY=audinux

dnf repoquery --repoid=copr:copr.fedorainfracloud.org:ycollet:$REPOSITORY --queryformat "%45{name} %{evr} %{buildtime}" | sort -r -k3 > packages-$RELEASE.txt
