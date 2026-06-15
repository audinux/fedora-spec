# kernel-xanmod

https://github.com/xanmod

XanMod is a general-purpose Linux kernel distribution with low-latency
patches, optimised scheduling (BORE), and performance tuning aimed at
desktop and audio workloads.

Set the Preemption Model to **Preemptible kernel (Low Latency)** in the
kernel configuration for best audio results.

## Preemption models available in XanMod

| Model | Config option | Use case |
|---|---|---|
| Preemptible (Low Latency) | `CONFIG_PREEMPT` | Desktop / audio — recommended |
| Full RT (if RT variant) | `CONFIG_PREEMPT_RT` | Pro audio, lowest latency |
| PREEMPT_DYNAMIC | `CONFIG_PREEMPT_DYNAMIC` | Default Fedora kernel |

The RT variant of XanMod (`kernel-xanmod-rt`) applies the full PREEMPT_RT
patchset and gives the lowest possible latency.

---

## Testing the kernel for low-latency audio

### 1. Verify the preemption model

```bash
uname -v
# Should contain PREEMPT or PREEMPT_RT depending on the variant

cat /sys/kernel/debug/sched/preemption_model 2>/dev/null
grep -i preempt /boot/config-$(uname -r)
```

### 2. Check RT scheduling is available

```bash
systemctl status rtkit-daemon
ulimit -r          # should return 95 (from audio-topology-profile limits.d)
chrt -f 10 sleep 1 && echo "RT scheduling OK"
```

### 3. Latency measurement with cyclictest

```bash
sudo dnf install rt-tests

sudo cyclictest --mlockall --smp --priority=80 \
    --interval=1000 --distance=0 --duration=10s --histogram=200
```

Expected results:

| Variant | Max latency idle | Max latency under load |
|---|---|---|
| XanMod PREEMPT | < 500 µs | < 2 ms |
| XanMod PREEMPT_RT | < 200 µs | < 500 µs |

### 4. Stress test: latency under system load

```bash
# Terminal 1: measure latency
sudo cyclictest --mlockall --smp --priority=80 \
    --interval=1000 --duration=60s --histogram=200

# Terminal 2: generate load
sudo dnf install stress-ng
stress-ng --cpu 0 --io 4 --vm 2 --vm-bytes 512M --timeout 60s
```

### 5. Audio-specific: PipeWire / JACK xrun test

```bash
pw-top                    # watch xrun counter for 5 min at idle
pw-top                    # watch xruns during stress-ng load
jack_iodelay              # measure round-trip JACK latency
pw-metadata -n settings 0 # check PipeWire quantum and rate
```

### 6. IRQ affinity and CPU governor (audio-topology-profile)

```bash
journalctl -t audio-topology          # check service ran correctly
taskset -cp $(pgrep -x pipewire)      # confirm pipewire on audio CPUs
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
for i in /proc/irq/*/smp_affinity_list; do echo "$i: $(cat $i)"; done
```

### 7. SMI (System Management Interrupts)

SMIs bypass even a full RT kernel and can cause latency spikes of
several milliseconds. Common on laptops.

```bash
sudo modprobe msr
sudo dnf install msr-tools
sudo rdmsr -p 0 0x34   # read before and after a cyclictest run
```

If the counter increases, disable unused hardware in BIOS (Bluetooth,
fingerprint reader, unused USB controllers) and apply firmware updates.

### 8. Summary checklist

```
[ ] uname -v shows PREEMPT or PREEMPT_RT
[ ] cyclictest max < 500 µs idle (PREEMPT) or < 200 µs (PREEMPT_RT)
[ ] cyclictest max < 2 ms under load (PREEMPT) or < 500 µs (PREEMPT_RT)
[ ] pw-top shows 0 xruns after 5 minutes idle
[ ] pw-top shows 0 xruns during stress-ng load
[ ] journalctl -t audio-topology shows correct CPU assignment
[ ] taskset confirms pipewire on audio CPUs
[ ] ulimit -r returns 95
[ ] SMI counter stable during cyclictest run
```
