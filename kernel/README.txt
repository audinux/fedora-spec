Use build_config.sh from fedora kernel spec repo:

$ wget https://mirrors.edge.kernel.org/pub/linux/kernel/v5.x/linux-5.10.8.tar.gz
$ wget https://cdn.kernel.org/pub/linux/kernel/projects/rt/5.6/older/patch-5.10.8-rt24.patch.gz
$ tar xvfz linux-5.10.8.tar.gz
$ gunzip patch-5.10.8-rt24.patch.gz
$ cd linux-5.10.8
$ patch -p1 < ../patch-5.10.8-rt24.patch

Since some kernel, I bypassed this step and just build vanilla RT kernels.

$ git clone https://src.fedoraproject.org/rpms/kernel.git
$ cd kernel
$ git switch f32
$ ./build_config.sh kernel-5.10.8

Copy kernel-5.10.8-x86_64.config as '.config' in the linux kernel source directory.

$ make xconfig

Since 5.6.*: check General setup -> Configure standard kernel features (expert users). This will toogle the "Fully preemptible kernel).

Enable CONFIG_PREEMPT_RT_FULL (menu General setup -> Preemption model -> Fully preemptible kernel).
Enable CONFIG_HZ_1000 (menu Processor type and features -> Timer frequency -> 1000 Hz).

Save the configuration file.

Copy back .config file into kernel-config-5.10.

To clean-up the boot menu:

$ grub2-mkconfig -o /boot/grub2/grub.cfg

Since 5.15.*:

Search for "CONFIG_HAVE_PREEMPT_DYNAMIC=y" in kernel-config* and replaces it by "CONFIG_HAVE_PREEMPT_DYNAMIC=n".

-------------------------------------------------------------------------------
Testing the RT kernel
-------------------------------------------------------------------------------

1. Verify the kernel is running in RT mode
-------------------------------------------

  $ uname -v
  # Should contain PREEMPT_RT

  $ cat /sys/kernel/debug/sched/preemption_model 2>/dev/null
  # Should return PREEMPT_RT

  $ grep -i preempt /boot/config-$(uname -r)
  # Should show CONFIG_PREEMPT_RT=y


2. Check RT scheduling is available for your user
--------------------------------------------------

  $ systemctl status rtkit-daemon
  $ ulimit -r
  # Should return 95 (set by audio-topology-profile limits.d)

  $ chrt -f 10 sleep 1 && echo "RT scheduling OK"


3. Latency measurement with cyclictest (most important test)
-------------------------------------------------------------

  $ sudo dnf install rt-tests

  # Quick test: 10 seconds at 1000 Hz, RT priority 80
  $ sudo cyclictest --mlockall --smp --priority=80 \
        --interval=1000 --distance=0 --duration=10s --histogram=200

  Expected results on a well-configured PREEMPT_RT system:
    Min latency : < 20 µs
    Avg latency : stable, close to min
    Max latency : < 200 µs idle, < 500 µs under load

  On a PREEMPT_RT kernel, max latency > 1 ms under load indicates
  a configuration problem (SMIs, wrong IRQ affinity, C-states, etc.).


4. Stress test: latency under system load
-----------------------------------------

  # Terminal 1: measure latency
  $ sudo cyclictest --mlockall --smp --priority=80 \
        --interval=1000 --duration=60s --histogram=200

  # Terminal 2: generate CPU, memory and I/O load
  $ sudo dnf install stress-ng
  $ stress-ng --cpu 0 --io 4 --vm 2 --vm-bytes 512M --timeout 60s

  Max latency under load is the most important single number.


5. Audio-specific: PipeWire / JACK xrun test
---------------------------------------------

  # Watch the xrun counter for 5 minutes at idle
  $ pw-top

  # Watch xruns under load (stress-ng running in parallel)
  $ pw-top

  # Measure round-trip JACK latency
  $ jack_iodelay

  # Check PipeWire quantum and sample rate
  $ pw-metadata -n settings 0


6. IRQ affinity and CPU governor (audio-topology-profile)
---------------------------------------------------------

  # Check audio-topology service applied its settings
  $ journalctl -t audio-topology

  # Confirm PipeWire is running on audio CPUs
  $ taskset -cp $(pgrep -x pipewire)

  # Confirm performance governor on audio CPUs
  $ cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

  # Confirm IRQs moved to non-audio CPUs
  $ for i in /proc/irq/*/smp_affinity_list; do echo "$i: $(cat $i)"; done


7. SMI (System Management Interrupts) — the hidden latency killer
------------------------------------------------------------------

  SMIs are non-maskable hardware interrupts that bypass the RT kernel
  entirely. They are common on laptops and can cause spikes of several ms.

  $ sudo modprobe msr
  $ sudo dnf install msr-tools

  # Read the SMI counter on CPU 0 before and after a 30s cyclictest run
  $ sudo rdmsr -p 0 0x34

  If the counter increases during the test, SMIs are firing.
  Mitigations: disable unused hardware in BIOS (Bluetooth, fingerprint
  reader, unused USB controllers), apply firmware updates.


8. Summary checklist
---------------------

  [ ] uname -v shows PREEMPT_RT
  [ ] cyclictest max < 200 µs idle
  [ ] cyclictest max < 500 µs under stress-ng load
  [ ] pw-top shows 0 xruns after 5 minutes idle
  [ ] pw-top shows 0 xruns during stress-ng load
  [ ] journalctl -t audio-topology shows correct CPU assignment
  [ ] taskset confirms pipewire on audio CPUs
  [ ] ulimit -r returns 95
  [ ] SMI counter stable during cyclictest run
