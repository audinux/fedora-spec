#!/bin/bash
set -e

CPUS=$(nproc --all)

# Priority 1: honour isolcpus= kernel parameter if present.
# Strip optional type flags (domain:, managed_irq, nohz, etc.) and keep
# only the numeric CPU list / ranges.
ISOLCPUS=$(grep -oE 'isolcpus=[^ ]+' /proc/cmdline 2>/dev/null | \
           cut -d= -f2- | \
           grep -oE '[0-9]+(-[0-9]+)?' | \
           paste -sd,)
if [ -n "$ISOLCPUS" ]; then
    echo "$ISOLCPUS"
    exit 0
fi

# Priority 2: Intel hybrid detection — prefer P-cores
detect_intel_layout() {
    local p_cores=""
    local e_cores=""

    for cpu in /sys/devices/system/cpu/cpu[0-9]*; do
        if [ -f "$cpu/topology/core_type" ]; then
            type=$(cat "$cpu/topology/core_type")
            if [ "$type" = "1" ]; then
                p_cores+=$(basename "$cpu" | sed 's/cpu//')","
            else
                e_cores+=$(basename "$cpu" | sed 's/cpu//')","
            fi
        fi
    done

    echo "$p_cores|$e_cores"
}

P_E=$(detect_intel_layout 2>/dev/null || echo "")
P_CORES=$(echo "$P_E" | cut -d'|' -f1 | sed 's/,$//')

# Priority 3: generic fallback based on CPU count
if [ -n "$P_CORES" ]; then
    AUDIO_CPUS="$P_CORES"
elif [ "$CPUS" -ge 8 ]; then
    AUDIO_CPUS="2-7"
elif [ "$CPUS" -ge 4 ]; then
    AUDIO_CPUS="2-3"
else
    AUDIO_CPUS=""
fi

echo "$AUDIO_CPUS"
