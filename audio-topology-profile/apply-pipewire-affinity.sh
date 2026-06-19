#!/bin/bash

LOG_TAG="audio-topology"

/usr/libexec/audio-topology-profile/detect.sh || exit 0

CPUS=$(/usr/libexec/audio-topology-profile/build-profile.sh)
[ -n "$CPUS" ] || exit 0

systemd-cat -t "$LOG_TAG" echo "Applying PipeWire CPU affinity: $CPUS"

# Write a runtime drop-in so the affinity survives pipewire restarts
DROPIN_DIR="${XDG_RUNTIME_DIR}/systemd/user/pipewire.service.d"
mkdir -p "$DROPIN_DIR"
printf '[Service]\nCPUAffinity=%s\n' "$CPUS" > "$DROPIN_DIR/10-audio-topology.conf"
systemctl --user daemon-reload

# Try set-property first (cgroup-level, affects all threads at once).
# Fall back to taskset on every PipeWire thread if set-property is not supported
# (older systemd or missing cgroup delegation).
if systemctl --user set-property pipewire.service CPUAffinity="$CPUS" 2>/dev/null; then
    systemd-cat -t "$LOG_TAG" echo "PipeWire CPUAffinity set via set-property: $CPUS"
else
    PW_PID=$(systemctl --user show -p MainPID --value pipewire.service 2>/dev/null || echo "")
    if [ -n "$PW_PID" ] && [ "$PW_PID" -gt 0 ] 2>/dev/null; then
        for tid in /proc/"$PW_PID"/task/*/; do
            taskset -cp "$CPUS" "$(basename "$tid")" 2>/dev/null || true
        done
        systemd-cat -t "$LOG_TAG" echo "PipeWire affinity set via taskset on all threads: $CPUS"
    else
        systemd-cat -t "$LOG_TAG" echo "PipeWire affinity: set-property failed and PipeWire PID not found"
    fi
fi
