#!/bin/bash

# Build spec for all the repositories and all the chroots

File=$1
copr-cli build --chroot fedora-35-x86_64 --chroot fedora-36-x86_64 audinux $File
