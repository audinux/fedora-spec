#!/bin/bash
set -e

# Require RT kernel
uname -v | grep -qi "PREEMPT_RT" || exit 1

# Require enough CPUs
CPUS=$(nproc --all)

if [ "$CPUS" -lt 4 ]; then
    exit 1
fi

exit 0
