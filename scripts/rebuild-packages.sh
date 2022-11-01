#!/bin/bash

# To get the API key required to use copr-cli, go to:
# https://copr.fedorainfracloud.org/api/

# The first packages to be built:
# premake*
# jmatconvol
# jnoisemeter
# libgig
# linuxsampler
# liblscp
# libaudec
# libcyaml
# libreproc
# libsmf
# libbacktrace-devel
# libcoverart
# lvtk
# portsmf
# redkit
# midimsg
# qscintilla
# sfArkLib
# cwiid
# non-ntk
# yaml-cpp03
# faust
# BatLib
# nanomsg
# ulfius
# ztoolkit
# JUCE*

# libgig before linuxsampler before liblscp
# non-ntk before ensemble-chorus
# veejay-core before veejay-server before veejay-gui
# sonic-pi after supercollider

# In Fedora now:
# Carla
# Cadence

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
    copr-cli build --chroot fedora-37-x86_64 --chroot fedora-37-aarch64 audinux $Files
done
