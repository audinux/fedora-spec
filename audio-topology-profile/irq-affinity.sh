#!/bin/bash

LOG_TAG="audio-topology"

/usr/libexec/audio-topology-profile/detect.sh || exit 0

TOTAL=$(nproc --all)
AUDIO_CPUS=$(/usr/libexec/audio-topology-profile/build-profile.sh)

[ -n "$AUDIO_CPUS" ] || exit 0

systemd-cat -t "$LOG_TAG" echo "Applying audio topology: audio CPUs=$AUDIO_CPUS"

# Expand a CPU list/range string ("0,4,8" or "2-7") to space-separated numbers.
# IFS must NOT be set to ',' inside the function body: doing so breaks the inner
# "for i in $(seq ...)" because seq outputs newlines, and with IFS=',' the entire
# newline-separated output is treated as one token, corrupting the result.
expand_cpulist() {
    local result=""
    local part i start end
    local -a parts
    IFS=',' read -ra parts <<< "$1"
    for part in "${parts[@]}"; do
        if [[ "$part" == *-* ]]; then
            start="${part%-*}"
            end="${part#*-}"
            for i in $(seq "$start" "$end"); do
                result="$result $i"
            done
        else
            result="$result $part"
        fi
    done
    echo "${result# }"
}

AUDIO_LIST=$(expand_cpulist "$AUDIO_CPUS")

# ── IRQ affinity: move all movable IRQs to non-audio CPUs ────────────────────
NON_AUDIO=""
for i in $(seq 0 $((TOTAL - 1))); do
    echo " $AUDIO_LIST " | grep -q " $i " || NON_AUDIO="${NON_AUDIO:+$NON_AUDIO,}$i"
done
[ -n "$NON_AUDIO" ] || NON_AUDIO="0"

for irq in /proc/irq/*/smp_affinity_list; do
    echo "$NON_AUDIO" > "$irq" 2>/dev/null || true
done

systemd-cat -t "$LOG_TAG" echo "IRQ affinity set: non-audio CPUs=$NON_AUDIO"

# ── threadirqs: set IRQ threads to SCHED_FIFO:1 so they stay below audio ────
# Only effective when the kernel is booted with threadirqs in the cmdline.
if grep -qw "threadirqs" /proc/cmdline 2>/dev/null; then
    systemd-cat -t "$LOG_TAG" echo "threadirqs active: setting IRQ threads to SCHED_FIFO:1"
    for pid in $(ps -eo pid,comm | awk '/irq\//{print $1}'); do
        chrt -f -p 1 "$pid" 2>/dev/null || true
    done
fi

# ── CPU frequency: set 'performance' governor on audio CPUs ─────────────────
# Prevents the scheduler from throttling cores mid-buffer on non-RT kernels.
for cpu in $AUDIO_LIST; do
    GOV="/sys/devices/system/cpu/cpu${cpu}/cpufreq/scaling_governor"
    if [ -f "$GOV" ]; then
        echo "performance" > "$GOV" 2>/dev/null || true
    fi
done

systemd-cat -t "$LOG_TAG" echo "CPU governor set to 'performance' on audio CPUs"
