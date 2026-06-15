#!/bin/bash

/usr/libexec/audio-topology-profile/detect.sh || exit 0

CPUS=$(/usr/libexec/audio-topology-profile/build-profile.sh)
[ -n "$CPUS" ] || exit 0

# Write a runtime drop-in so the affinity survives pipewire restarts
DROPIN_DIR="${XDG_RUNTIME_DIR}/systemd/user/pipewire.service.d"
mkdir -p "$DROPIN_DIR"
printf '[Service]\nCPUAffinity=%s\n' "$CPUS" > "$DROPIN_DIR/10-audio-topology.conf"
systemctl --user daemon-reload

# Apply immediately to the already-running pipewire instance
systemctl --user set-property pipewire.service CPUAffinity="$CPUS" 2>/dev/null || true
