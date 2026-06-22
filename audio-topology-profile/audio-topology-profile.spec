# Status: active
# Tag: Tool
# Type: Standalone
# Category: Tool

Name: audio-topology-profile
Version: 1.0
Release: 6%{?dist}
Summary: CPU topology aware audio tuning for PipeWire/JACK
License: MIT
BuildArch: noarch

BuildRequires: systemd-rpm-macros

Source0: detect.sh
Source1: build-profile.sh
Source2: irq-affinity.sh
Source3: apply-pipewire-affinity.sh
Source4: audio-topology.service
Source5: audio-topology-user.service
Source6: 90-audio-topology.conf

Requires: systemd
Requires: pipewire
Requires: util-linux
Requires: procps-ng

%description
Dynamic low-latency audio tuning profile for PipeWire/JACK.
On PREEMPT_RT or PREEMPT_DYNAMIC kernels with at least 4 CPUs,
it pins IRQs to non-audio CPUs (system service, requires root)
and sets PipeWire's CPU affinity to the optimal core set
(user service, no root required).

CPU topology is detected automatically using the following priority:
  1. isolcpus= kernel parameter, if set by the user
  2. Intel hybrid P-cores (Alder Lake / Raptor Lake / Meteor Lake)
  3. Generic fallback: CPUs 2-7 (>=8 cores) or CPUs 2-3 (4-7 cores)

Additional tuning applied by the system service:
  - IRQ threads are set to SCHED_FIFO:1 when the kernel is booted
    with threadirqs, keeping them schedulable but below audio threads
  - The 'performance' CPU frequency governor is set on audio CPUs
    to prevent mid-buffer throttling

PAM limits for the 'audio' group (rtprio, memlock, nice) are installed
to allow RT scheduling and memory locking.
Note: PipeWire's own threads already obtain RT priority through rtkit
and do not need these limits. However, JACK client applications running
through pipewire-jack request RT priority for their own threads directly,
bypassing rtkit. Members of the 'audio' group therefore still need these
limits for Ardour, Carla, and other JACK clients to run their audio
threads at RT priority without requiring root privileges.

%prep

%build

%install

install -m 0755 -d %{buildroot}/%{_libexecdir}/audio-topology-profile/
install -m 0755 -d %{buildroot}/%{_unitdir}/
install -m 0755 -d %{buildroot}/%{_userunitdir}/
install -m 0755 -d %{buildroot}/%{_userunitdir}/pipewire.service.wants/
install -m 0755 -d %{buildroot}/%{_sysconfdir}/security/limits.d/

install -m 0755 %{SOURCE0} %{buildroot}/%{_libexecdir}/audio-topology-profile/
install -m 0755 %{SOURCE1} %{buildroot}/%{_libexecdir}/audio-topology-profile/
install -m 0755 %{SOURCE2} %{buildroot}/%{_libexecdir}/audio-topology-profile/
install -m 0755 %{SOURCE3} %{buildroot}/%{_libexecdir}/audio-topology-profile/
install -m 0644 %{SOURCE4} %{buildroot}/%{_unitdir}/
install -m 0644 %{SOURCE5} %{buildroot}/%{_userunitdir}/
install -m 0644 %{SOURCE6} %{buildroot}/%{_sysconfdir}/security/limits.d/

# Create the WantedBy symlink so the user service is auto-enabled for all users
# without requiring "systemctl --user enable audio-topology-user.service"
ln -s ../audio-topology-user.service \
    %{buildroot}/%{_userunitdir}/pipewire.service.wants/audio-topology-user.service

%post
%systemd_post audio-topology.service
# Auto-enable and start the system service: it is purpose-built to run on every
# boot and there is no reason for an administrator to opt out selectively.
systemctl enable audio-topology.service >/dev/null 2>&1 || :
systemctl start  audio-topology.service >/dev/null 2>&1 || :
%systemd_user_post audio-topology-user.service
echo ""
echo "NOTE: The RT priority limits installed by this package apply to members"
echo "of the 'audio' group. If your user account is not already in that group,"
echo "run the following command and then log out and back in:"
echo ""
echo "  sudo usermod -aG audio \$USER"
echo ""
echo "This is required for JACK client applications (Ardour, Carla, etc.)"
echo "running through pipewire-jack to obtain RT priority for their audio threads."
echo ""

%preun
%systemd_preun audio-topology.service
%systemd_user_preun audio-topology-user.service

%postun
%systemd_postun_with_restart audio-topology.service
%systemd_user_postun audio-topology-user.service

%files
%{_libexecdir}/audio-topology-profile/
%{_unitdir}/audio-topology.service
%{_userunitdir}/audio-topology-user.service
%{_userunitdir}/pipewire.service.wants/audio-topology-user.service
%{_sysconfdir}/security/limits.d/90-audio-topology.conf

%changelog
* Mon Jun 22 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-6
- spec: auto-enable and start audio-topology.service in %post so the system
  service (IRQ affinity, CPU governor) runs on every boot without requiring
  a manual "systemctl enable audio-topology.service" after install

* Sun Jun 21 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-5
- irq-affinity.sh: fix expand_cpulist() IFS bug — local IFS=',' contaminated
  the inner "for i in $(seq ...)" loop, treating all seq output as one token
  with embedded newlines; NON_AUDIO was wrongly set to all CPUs
- apply-pipewire-affinity.sh: add systemd-cat logging; add taskset fallback
  on all PipeWire threads when set-property is not supported
- spec: install pipewire.service.wants/ symlink so user service is auto-enabled
  without requiring "systemctl --user enable";

* Wed Jun 17 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-4
- detect.sh: fix PREEMPT_DYNAMIC detection — only enable tuning when
  booted with preempt=full; without it PREEMPT_DYNAMIC runs in voluntary
  preemption mode and gives no latency benefit over a standard kernel

* Mon Jun 15 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-3
- build-profile.sh: add isolcpus= kernel parameter as highest-priority CPU source
- irq-affinity.sh: set IRQ threads to SCHED_FIFO:1 when threadirqs is active;
  set 'performance' CPU governor on audio CPUs; add systemd journal logging
- Add 90-audio-topology.conf: PAM limits for @audio group (rtprio, memlock, nice)
- Add procps-ng dependency (ps, used by irq-affinity.sh)

* Mon Jun 15 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-2
- Fix detect.sh: CPUS was used before being defined; add PREEMPT_DYNAMIC detection
- Fix irq-affinity.sh: use build-profile.sh for dynamic CPU selection; use
  smp_affinity_list instead of smp_affinity; call detect.sh unconditionally
- Fix audio-topology.service: remove ConditionKernelCommandLine; add RemainAfterExit
- Replace static 10-audio-topology.conf drop-in with apply-pipewire-affinity.sh
  and audio-topology-user.service for dynamic, kernel-aware PipeWire affinity

* Mon Jun 15 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial version of the spec
