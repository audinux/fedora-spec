#!/bin/bash

CPUS=$(nproc --all)

# Require at least 4 CPUs
[ "$CPUS" -ge 4 ] || exit 1

# Require a PREEMPT_DYNAMIC or PREEMPT_RT kernel
uname -v | grep -qiE "PREEMPT_RT|PREEMPT_DYNAMIC" || exit 1

exit 0
