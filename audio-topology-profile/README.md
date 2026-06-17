# audio-topology-profile

Dynamic low-latency audio tuning for PipeWire and JACK on Fedora.

## What it does

The package installs two systemd services and a PAM limits file that together
apply several layers of tuning at boot and at user login.

### System service — `audio-topology.service` (runs as root)

Activated at boot with at least 4 CPUs and one of the following conditions:

- Kernel reports `PREEMPT_RT` in `uname -v` — always fully preemptible,
  no extra configuration needed.
- Kernel reports `PREEMPT_DYNAMIC` in `uname -v` **and** the kernel was
  booted with `preempt=full` on the cmdline. Without `preempt=full`,
  a `PREEMPT_DYNAMIC` kernel (the Fedora default) runs in voluntary
  preemption mode, which gives no latency benefit over a standard kernel
  and is therefore skipped.

On kernels that do not meet these conditions the service exits cleanly
without doing anything.

**CPU set selection** (`build-profile.sh`) — priority order:

1. `isolcpus=` kernel parameter, if present in `/proc/cmdline`. When the
   user has already isolated CPUs at the kernel level, those are the best
   possible choice and are used as-is.
2. Intel hybrid P-cores (Alder Lake / Raptor Lake / Meteor Lake), detected
   via `/sys/devices/system/cpu/cpuN/topology/core_type`. P-cores have
   larger caches and more predictable latency than E-cores.
3. Generic fallback: CPUs 2–7 on systems with ≥ 8 cores, CPUs 2–3 on
   systems with 4–7 cores. CPU 0 and 1 are left for the kernel and IRQs.

**IRQ affinity** (`irq-affinity.sh`):

- All movable IRQs are pinned to the non-audio CPUs via
  `/proc/irq/*/smp_affinity_list`, reducing interrupt-driven jitter on
  the audio processing cores.
- If the kernel was booted with `threadirqs`, IRQ handler threads are set
  to `SCHED_FIFO` priority 1. This makes them schedulable by the RT
  scheduler while keeping them below audio threads (which run at priority
  70–95 with PipeWire/JACK).
- The `performance` CPU frequency governor is set on audio CPUs to prevent
  the hardware from throttling mid-buffer. This is most impactful on
  laptops and AMD systems with aggressive power management.

All actions are logged to the systemd journal under the `audio-topology`
tag and can be reviewed with:

```
$ journalctl -t audio-topology
```

### User service — `audio-topology-user.service` (runs as the logged-in user)

Starts automatically after `pipewire.service` in the user session and
re-runs whenever PipeWire restarts.

- Calls `detect.sh` — exits cleanly if the kernel or CPU count does not
  meet the requirements.
- Calls `build-profile.sh` to determine the audio CPU set.
- Writes a runtime drop-in to
  `$XDG_RUNTIME_DIR/systemd/user/pipewire.service.d/10-audio-topology.conf`
  so the affinity survives PipeWire restarts within the session.
- Calls `systemctl --user set-property pipewire.service CPUAffinity=…` to
  apply the affinity immediately to the already-running PipeWire instance.

### PAM limits — `/etc/security/limits.d/90-audio-topology.conf`

```
@audio - rtprio  95
@audio - memlock unlimited
@audio - nice    -19
```

PipeWire's own threads already obtain RT priority through `rtkit-daemon`
and do not need these limits. However, **JACK client applications** running
through `pipewire-jack` (Ardour, Carla, Hydrogen, etc.) request RT priority
for their own audio threads directly via the JACK API, bypassing rtkit.
Those threads run inside the client process, not inside PipeWire, so rtkit
is not involved. Members of the `audio` group need these limits for JACK
clients to run at RT priority without root privileges.

Make sure your user account is in the `audio` group:

```
$ sudo usermod -aG audio $USER
```

Log out and back in for the change to take effect.

## PipeWire + pipewire-jack vs PipeWire + standard JACK

Understanding which JACK stack you are running matters for getting RT priority
right. The two setups behave very differently under the hood.

### PipeWire + pipewire-jack (recommended on Fedora)

`pipewire-jack` replaces the JACK client libraries (`libjack.so`) with shims
that redirect JACK API calls into PipeWire's built-in JACK server. No separate
`jackd` process runs.

```
Application → libjack shim → PipeWire (built-in JACK server)
```

**RT priority path:**
- PipeWire's own processing threads → elevated by **rtkit** automatically.
  No `limits.d` needed for PipeWire itself.
- JACK client audio threads (inside Ardour, Carla, etc.) → the shim calls
  `pthread_setschedparam()` directly in the **application's process**.
  rtkit is not involved. The application must already have permission to
  set RT priority, which comes from the **`@audio` limits.d entry**.
- This is why `@audio - rtprio 95` is still necessary even on a
  pipewire-only system if you run any JACK client application.

**Memory locking:**
- PipeWire locks its own buffers via rtkit.
- JACK clients call `mlockall()` directly. Again, `@audio - memlock unlimited`
  is required for this to succeed without root.

**Latency characteristics:**
- PipeWire manages the audio graph and scheduling, so buffer sizes and
  latency are configured via PipeWire (`/etc/pipewire/pipewire.conf` or
  `~/.config/pipewire/`).
- Typical achievable latency: 2–5 ms on a PREEMPT_DYNAMIC kernel,
  sub-millisecond on PREEMPT_RT.

### PipeWire + standard JACK (jackd/jackdbus)

In this setup, a real `jackd` process runs alongside PipeWire. PipeWire
connects to JACK as a client (or the two are bridged via `pw-jack`), and
`jackd` owns the audio hardware directly.

```
Application → libjack → jackd process → audio hardware
                              ↕
                         PipeWire (as JACK client, for other apps)
```

**RT priority path:**
- `jackd` elevates its own threads and the threads of connected clients
  using one of three mechanisms, in order of preference:
  1. **D-Bus + rtkit** — if `jackd` was compiled with rtkit support and
     rtkit-daemon is running. No `limits.d` needed.
  2. **`@audio` limits.d** — if rtkit is not available or not used.
     `jackd` calls `pthread_setschedparam()` directly, which requires
     the process to have `RLIMIT_RTPRIO > 0`.
  3. **setuid wrapper** (`jackd` installed setuid root) — legacy approach,
     no longer used on modern Fedora.
- JACK client audio threads follow the same rules as in the pipewire-jack
  case: they call `pthread_setschedparam()` in their own process and need
  the `@audio` limits to succeed.

**Latency characteristics:**
- `jackd` has a more direct path to the hardware (ALSA, no PipeWire graph
  in between), which can give slightly more predictable latency at very
  small buffer sizes.
- However, PipeWire-native applications (browsers, video players) do not
  participate in the JACK graph and may cause xruns if they access the
  sound card concurrently unless the bridge is configured carefully.

### Summary table

| | PipeWire + pipewire-jack | PipeWire + standard JACK |
|---|---|---|
| Separate jackd process | No | Yes |
| PipeWire RT priority | rtkit | rtkit |
| JACK client RT priority | `@audio` limits.d | `@audio` limits.d (or rtkit if jackd supports it) |
| `@audio` group needed | **Yes** | **Yes** |
| Hardware access | PipeWire owns it | jackd owns it |
| PipeWire-native apps | Seamless | Require bridge |
| Recommended on Fedora | **Yes** | Only for specific workflows |

**Bottom line:** regardless of which JACK stack you use, members of the
`audio` group and the `limits.d` file installed by this package are needed
for JACK client applications to run their audio threads at RT priority.

## When does this help most?

| Setup | Benefit |
|---|---|
| PREEMPT_RT or linux-lqx / linux-xanmod kernel | High — full RT scheduling, affinity and IRQ isolation all combine |
| Intel hybrid CPU (Alder Lake+) on any kernel | Medium-high — P-core pinning avoids E-core cache/latency variance |
| Standard PREEMPT_DYNAMIC kernel, homogeneous CPU | Low — CPU affinity without true isolation has limited effect; consider adding `isolcpus=` to the kernel cmdline |

For maximum benefit on a standard Fedora kernel, add the following to your
kernel cmdline (adjust CPU numbers to match your system):

```
isolcpus=2-7 threadirqs
```

`isolcpus` keeps the general-purpose scheduler off the audio CPUs entirely.
`threadirqs` makes IRQ handlers schedulable so their priority can be
lowered relative to audio threads.

## Verification

```bash
# Check which CPUs PipeWire is allowed to run on
$ taskset -cp $(pgrep -x pipewire)

# Confirm the runtime drop-in was written
$ cat $XDG_RUNTIME_DIR/systemd/user/pipewire.service.d/10-audio-topology.conf

# Check the user service ran correctly
$ systemctl --user status audio-topology-user.service

# Check the system service (IRQ affinity, governor, threadirqs)
$ systemctl status audio-topology.service

# Review all actions taken at boot
$ journalctl -t audio-topology

# Check PipeWire thread scheduling and CPU assignment
$ ps -eLo pid,tid,psr,cls,rtprio,comm | grep pipewire
```
