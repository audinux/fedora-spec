#!/bin/bash

File=$1
copr-cli build --chroot fedora-45-x86_64 --chroot fedora-45-aarch64 audinux $File
