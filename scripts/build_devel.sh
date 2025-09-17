#!/bin/bash

File=$1
copr-cli build --chroot fedora-rawhide-x86_64 --chroot fedora-rawhide-aarch64 audinux $File
