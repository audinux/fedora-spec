#!/bin/bash
set -e

CPUS=$(nproc --all)

# Intel hybrid detection
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
E_CORES=$(echo "$P_E" | cut -d'|' -f2 | sed 's/,$//')

# Prefer Intel P-cores if available
if [ -n "$P_CORES" ]; then
    AUDIO_CPUS="$P_CORES"

# Generic fallback
elif [ "$CPUS" -ge 8 ]; then
    AUDIO_CPUS="2-7"

elif [ "$CPUS" -ge 4 ]; then
    AUDIO_CPUS="2-3"

else
    AUDIO_CPUS=""
fi

echo "$AUDIO_CPUS"
