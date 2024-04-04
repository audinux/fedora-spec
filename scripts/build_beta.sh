#!/bin/bash

# Build spec for all the repositories and all the chroots

File=$1
copr-cli build --chroot fedora-rawhide-x86_64 --chroot fedora-rawhide-aarch64 audinux $File
