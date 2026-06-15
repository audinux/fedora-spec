# kernel-lqx (Liquorix)

https://github.com/damentz/liquorix-package/
https://github.com/zen-kernel/zen-kernel

Liquorix is a distro kernel replacement built from the Zen kernel patchset.
It targets desktop responsiveness and low-latency audio with an aggressive
scheduler configuration (MuQSS / BORE depending on version), a 1000 Hz
timer, and full voluntary preemption enabled by default.

## Key configuration differences from the stock Fedora kernel

| Setting | Stock Fedora | Liquorix |
|---|---|---|
| Preemption model | PREEMPT_DYNAMIC | PREEMPT (full voluntary) |
| Timer frequency | 250 Hz | 1000 Hz |
| Scheduler | CFS | Zen / BORE |
| I/O scheduler | mq-deadline | BFQ |

Liquorix is **not** a full PREEMPT_RT kernel. For the lowest possible
latency (sub-100 µs), use `kernel-xanmod-rt` or the `kernel` (PREEMPT_RT)
package from this repository instead.

---

## Testing the kernel for low-latency audio

### 1. Verify the kernel and preemption model

```bash
uname -r    # should contain lqx
uname -v    # should contain PREEMPT

grep -i preempt /boot/config-$(uname -r)
# CONFIG_PREEMPT=y
# CONFIG_HZ_1000=y
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

Expected results on a well-configured Liquorix system:

| Metric | Expected value |
|---|---|
| Min latency | < 50 µs |
| Max latency (idle) | < 500 µs |
| Max latency (under load) | < 2 ms |

Values above 2 ms under load suggest IRQ affinity or C-state issues.
For sub-200 µs max latency, switch to a full PREEMPT_RT kernel.

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

On a non-RT kernel like Liquorix, IRQ affinity and CPU pinning have a
bigger relative impact than on PREEMPT_RT — they are worth tuning carefully.

```bash
journalctl -t audio-topology          # check service ran correctly
taskset -cp $(pgrep -x pipewire)      # confirm pipewire on audio CPUs
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
for i in /proc/irq/*/smp_affinity_list; do echo "$i: $(cat $i)"; done
```

Adding `isolcpus=` and `threadirqs` to the kernel cmdline gives the most
improvement on a non-RT kernel — see the audio-topology-profile README.

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
[ ] uname -r contains lqx
[ ] uname -v shows PREEMPT
[ ] cyclictest max < 500 µs idle
[ ] cyclictest max < 2 ms under load
[ ] pw-top shows 0 xruns after 5 minutes idle
[ ] pw-top shows 0 xruns during stress-ng load
[ ] journalctl -t audio-topology shows correct CPU assignment
[ ] taskset confirms pipewire on audio CPUs
[ ] ulimit -r returns 95
[ ] SMI counter stable during cyclictest run
```
