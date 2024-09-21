#!/bin/bash

# Build spec for all the repositories and all the chroots

File=$1
copr-cli build --chroot fedora-41-x86_64 --chroot fedora-41-aarch64 audinux $File
