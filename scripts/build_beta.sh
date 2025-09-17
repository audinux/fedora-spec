#!/bin/bash

File=$1
copr-cli build --chroot fedora-43-x86_64 --chroot fedora-43-aarch64 audinux $File
