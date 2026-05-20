#!/bin/bash
set -e

# CPU2 affinity mask
MASK=4

for irq in /proc/irq/*/smp_affinity; do
    echo $MASK > "$irq" 2>/dev/null || true
done
