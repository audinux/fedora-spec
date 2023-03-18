#!/bin/bash

# Build spec for all the repositories and all the chroots

File=$1
copr-cli build --chroot fedora-36-x86_64 --chroot fedora-37-x86_64 --chroot fedora-37-aarch64 --chroot fedora-38-x86_64 --chroot fedora-38-aarch64 audinux $File
