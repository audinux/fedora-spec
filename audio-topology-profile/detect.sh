#!/bin/bash
set -e

# minimum viable audio machine
[ "$CPUS" -ge 4 ] || exit 1

# Require RT kernel
grep -qw "preempt=full" /proc/cmdline && AUDIO_OK=1
uname -v | grep -qi PREEMPT_RT && AUDIO_OK=1
[ -n "$AUDIO_OK" ] || exit 1

# Require enough CPUs
CPUS=$(nproc --all)

exit 0
