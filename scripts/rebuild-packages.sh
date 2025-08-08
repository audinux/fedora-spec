#!/bin/bash

# To get the API key required to use copr-cli, go to:
# https://copr.fedorainfracloud.org/api/

# The first packages to be built:
# premake3-3.7-2.fc41.src.rpm
# premake4-4.4beta5-1.fc41.src.rpm
# premake5-5.0.0beta5-1.fc41.src.rpm
# jmatconvol-0.5.2-1.fc41.src.rpm
# libgig-4.3.0-1.fc41.src.rpm
# linuxsampler-2.1.1-2.fc41.src.rpm
# liblscp-0.9.4-1.fc41.src.rpm
# libaudec-devel-0.3.4-1.fc41.src.rpm
# libcyaml-1.4.2-1.fc41.src.rpm
# libreproc-14.2.0-1.fc41.src.rpm
# libsmf-1.4-8.fc41.src.rpm
# libbacktrace-devel-0.0.1-1.fc41.src.rpm
# libcoverart-1.0.0-4.fc41.src.rpm
# python2.7-2.7.18-43.fc41.src.rpm
# lvtk-2.0.0.6bfe981-4.fc41.src.rpm
# portsmf-0.1-2.fc41.src.rpm
# midimap.lv2-0.4.4-1.fc41.src.rpm
# qscintilla-2.14.1-2.fc41.src.rpm
# cwiid-0.6.00-36.20100505gitfadf11.fc41.src.rpm
# vst3sdk-3.7.13-1.fc41.src.rpm
# sfizz-1.2.3-4.fc41.src.rpm
# sfizz-ui-1.2.3-1.fc41.src.rpm
# yaml-cpp03-0.3.0-15.fc41.src.rpm
# faust-2.79.3-39.fc41.src.rpm
# ulfius-2.7.2-1.fc41.src.rpm
# ztoolkit-0.1.2-1.fc41.src.rpm
# JUCE5-5.4.7-2.fc41.src.rpm
# JUCE60-6.0.8-5.fc41.src.rpm
# JUCE61-6.1.6-6.fc41.src.rpm
# JUCE7-7.0.12-10.fc41.src.rpm
# JUCE-8.0.6-10.fc41.src.rpm
# hvcc-0.13.2-2.fc41.src.rpm
# clap-1.2.6-1.fc41.src.rpm
# liquidsfz-0.3.2-2.fc41.src.rpm
# kernel-lqx-mao-6.11.10.lqx1-14.fc41.src.rpm
# kernel-rt-mao-6.6.65.rt47-13.fc41.src.rpm
# kernel-xan-mao-6.11.10.xan1-12.fc41.src.rpm
# librearp-2.5-2.fc41.src.rpml
# ibtess2-1.0.2-1.fc41.src.rpm
# libtimecode-0.1.0-1.fc41.src.rpm

# libgig before linuxsampler before liblscp
# non-ntk before ensemble-chorus
# veejay-core before veejay-server before veejay-gui
# sonic-pi after supercollider

# In Fedora now:
# Carla
# Cadence

#
# Chec API token expiration before starting
#

################
# Package List #
################

#######################
# End of Package List #
#######################

# Reorder srpm file in FILELIST: dependencies first

FILELIST=""

# --chroot fedora-rawhide-x86_64 --chroot fedora-rawhide-aarch64

for Files in $FILELIST
do
    copr-cli build --chroot fedora-42-x86_64 --chroot fedora-42-aarch64 audinux tmp/$Files
done
