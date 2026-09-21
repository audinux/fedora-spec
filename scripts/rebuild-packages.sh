#!/bin/bash

VERSION=45
# To get the API key required to use copr-cli, go to:
# https://copr.fedorainfracloud.org/api/

################
# Package List #
################

#######################
# End of Package List #
#######################

# Reorder srpm file in FILELIST: dependencies first

FILELIST=""

for Files in $FILELIST
do
    copr-cli build --chroot fedora-$VERSION-x86_64 --chroot fedora-$VERSION-aarch64 audinux tmp/$Files
done
