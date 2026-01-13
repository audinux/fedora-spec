#!/bin/bash

File=$1
copr-cli build --chroot fedora-44-x86_64 --chroot fedora-44-aarch64 audinux $File
