#!/bin/bash

CPUS=$(nproc --all)

# Require at least 4 CPUs
[ "$CPUS" -ge 4 ] || exit 1

# Require a kernel running in full preemption mode:
#   - PREEMPT_RT: always fully preemptible, no extra cmdline needed
#   - PREEMPT_DYNAMIC: only fully preemptible when booted with preempt=full
#     (without it, PREEMPT_DYNAMIC defaults to voluntary preemption, which
#     is equivalent to a standard desktop kernel and gives no latency benefit)
if uname -v | grep -qi "PREEMPT_RT"; then
    exit 0
fi

if uname -v | grep -qi "PREEMPT_DYNAMIC"; then
    grep -qw "preempt=full" /proc/cmdline || exit 1
    exit 0
fi

exit 1
