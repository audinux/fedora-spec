# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Pau Aliagas <linuxnow@gmail.com>
Name: omx-dsp
Version: 0.28.0
Release: 1%{?dist}
License: GPL-3.0-or-later
Summary: The audio toolbox of the OpenMixer console, as a real-time-safe C library
URL: https://github.com/FreeMixer/omx-dsp

Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: binutils
BuildRequires: gawk
BuildRequires: diffutils
BuildRequires: pkgconfig
BuildRequires: omx-contract-devel >= 3.1.0

# Headers and a static archive only: nothing of this package is loaded at run time.
%global debug_package %{nil}
# A static archive carries machine code only, never LTO bytecode a consumer's compiler cannot read.
%global _lto_cflags %{nil}

%description
libomxdsp is the sound of the OpenMixer console, as a library: the filters,
envelopes, delays, limiters, gates, compressors and other building blocks of a
mixer channel, written in plain C that never allocates, locks or calls the
system while audio is running. The console and the omx plugins are built from
this same code, so an effect sounds the same on the desk and in your DAW, sample
for sample. Link it into your own plugin, effect or audio tool and start from
parts that are already tested against exact results at every sample rate.

%package devel
Summary: Headers and static library to build on the OpenMixer audio toolbox
Provides: %{name}-static = %{version}-%{release}
Requires: omx-contract-devel >= 3.1.0
Requires: %{name}-contract = %{version}-%{release}

%package contract
Summary: omx-dsp's kernel and instance declarations, for programs that read them at run time
BuildArch: noarch
# the declarations live in omx-contract's contract directory and are read against its schema; a floor only
Requires: omx-contract-data >= 3.1.0

%description contract
omx-dsp's package of omx-contract's contract directory: the declarations of
its kernels and instance faces (their controls, units and readouts) under
/usr/share/omx-contract/contract.d/3/omx-dsp. A program that reads them while
it runs (a panel, the omx-contract command) needs this package, not the
development one.

%description devel
Everything you need to build against libomxdsp: the headers under
include/omxdsp and the static library in three flavours, each with its
pkg-config file: libomxdsp.a (omxdsp), libomxdsp-contracts.a
(omxdsp-contracts, contracts compiled in) and libomxdsp-tsan.a (omxdsp-tsan,
contracts and ThreadSanitizer). Programs link the library statically; no shared
library exists.

%prep
%autosetup

%build
%set_build_flags
%make_build lib

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} INCLUDEDIR=%{_includedir}

%check
%make_build test

%files devel
%license LICENSE
%doc README.md BUILDING.md
%{_includedir}/omxdsp/
%{_libdir}/libomxdsp.a
%{_libdir}/libomxdsp-contracts.a
%{_libdir}/libomxdsp-tsan.a
%{_libdir}/pkgconfig/omxdsp.pc
%{_libdir}/pkgconfig/omxdsp-contracts.pc
%{_libdir}/pkgconfig/omxdsp-tsan.pc
%{_bindir}/omx-dsp-copy-check
%{_mandir}/man1/omx-dsp-copy-check.1*
%{_datadir}/omxdsp/

%files contract
%license LICENSE
%{_datadir}/omx-contract/contract.d/3/omx-dsp/

%changelog
* Sun Nov 01 2026 Pau Aliagas <linuxnow@gmail.com> - 0.28.0-1
- New faces, each with closed-form oracles at the nine rates: clipper, upward
  (an upward compressor), glue (a bus compressor), loudlevel (a leveler to a
  LUFS target), balancer (a spectral balancer), spring (a spring reverb).
- plosive sensitivityDb and popSensitivityDb come up at 16 dB, above the
  steady contrast of a buzzy vowel. The leveler's table and width's comb and
  bass mono stand as declared; none of these is provisional now.
- The delay face takes its read taps: fxDelayTaps, tap0..3 gain and pan and
  tap1..3Factor; resolve() gains those twelve arguments after pingpong.
- New: mix/omx_slew.h, a gain that crosses a declared time instead of one
  block, omx_slew_step, omx_slew_gain and omx_slew_hold (the fade a rewire
  needs), with closed-form oracles and digests at the nine rates (#235).
- New: MIXMATRIX_PERIOD_SHARE, 0.2 of the period, and make bench-mixmatrix
  holds a 64 x 32 matrix to it at the nine rates.
- New: omx_round_half_up, and fx/omx_instance_io.h, the opening and the
  bypass check of the instance faces.
- comp attackMs steps 0.1 and releaseMs 5, eq notchQ 0.1: each stepped from
  its minimum missed its own default or maximum.
- The EQ kinds, the low-pass hand-over and the HRP family tables read their
  declarations; no value moves.
- tools/clone-check.sh and tools/travel-grid-check.sh, each with its sabotage.
- The reverb's de-esser arm reads its level off the stimulus.

* Sat Oct 31 2026 Pau Aliagas <linuxnow@gmail.com> - 0.27.1-1
- omx_idelay_samples() no longer casts a float past the range of uint32_t:
  a delay far beyond the ring now clamps to the last slot (#263).
- The comments say decision where they said ruling (#252).

* Fri Oct 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.27.0-1
- New sections and faces: omx_width (M/S width, complementary comb, bass mono)
  and its instance face, the tone face (tilt span and the DJ filter map,
  FX-9), and the leveler, the plosive tamer, the upward law of omx_dyn, the
  compressor's release modes and effective-attack readout, and the
  sub-octaver (FX-10 to FX-13, FX-16, FX-17); omx_envelope and omx_gaincomp
  grow with them (#188).
- Dependency floors come from packaging/deps.txt, one file for both
  packages; a check refuses a new public name in a patch release.
- The package jobs in CI install python3 (#253).

* Sun Oct 25 2026 Pau Aliagas <linuxnow@gmail.com> - 0.26.0-1
- New sections: omx_tilt (a first-order shelf pair about one pivot),
  omx_duck (the wet ducker, omx_duck_step), omx_doppler (a detuning read
  head on the fractional delay) and omx_band_dyn_design() (design B).
- New instance faces: the dynamic EQ (dyneq), the multiband compressor
  (mbcomp) and the vocal doubler (doubler). The compressor gains the key
  path, hold and ducker; the gate gains key listen and key tilt; the delay
  gains tempo sync, tape and analog modes and the wet duck; the reverb
  gains early reflections, tail level, wet duck and wet de-ess.
- New kernel definitions doubler.json and dyneq.json; band_dyn, comp,
  delay, gate, mbcomp and reverb grow their controls and readouts. The
  dynamics kernels' key tilt is a slope in dB/oct, a unit omx-contract
  3.1.0 adds, so the floor is omx-contract-devel >= 3.1.0.
- The package build runs make test at dpkg's parallel level again; the
  gen-once check reads its list from a file, not from make's stdout.

* Tue Oct 20 2026 Pau Aliagas <linuxnow@gmail.com> - 0.25.0-1
- Built against omx-contract 3.0.0, the schema's major 3: data/ installs
  under contract.d/3/omx-dsp/ and every definition file requires
  omx-contract-schema >= 3.0.0.
- The second C spellings of eight travels (their c.alias) are gone:
  OMX_PAN_PAN_*, OMX_DELAY_TIME_MS_*, OMX_DELAY_TAPS_* and OMX_DRIVE_*_*.
  Read PAN_RANGE as OMX_PAN_RANGE_MIN/MAX and the others by their
  travels' own names.
- New header omxdsp/omx_eq_defaults.h: omx_eq_default_centres and
  omx_eq_default_type, the one default rule for the bands of a fresh EQ,
  moved from omx-contract's header with the same results for every band
  count; make eq-default-bands holds them to the rule's answers.
- omx-contract-devel >= 3.0.0.

* Mon Oct 19 2026 Pau Aliagas <linuxnow@gmail.com> - 0.24.1-1
- 0.24.0 has no arm64 DEB: its trixie arm64 build passed the release's job time
  limit, which is now 90 minutes.
- A release dispatched by hand builds the arm64 and aarch64 packages too.

* Sun Oct 18 2026 Pau Aliagas <linuxnow@gmail.com> - 0.24.0-1
- Nine instance faces (drive, rotary, reverb, chorus, deesser, delay, eq,
  flanger and limiter) accept the nine oracle rates from 32 to 192 kHz, the
  contract's OMX_ORACLE_FULL_RATES, as the pitch faces do; at 32, 64 and
  128 kHz they used to pass the signal through. Their oracles run every
  arm at the nine rates.
- The deesser designs its detector band at no more than
  DEESS_NYQUIST_FRACTION (0.91, declared in data/kernels/deesser.json) of
  Nyquist, so at 32 kHz the band-pass keeps stable poles. No design at a
  declared rate moves.
- The cookbook low-pass holds its corner below Nyquist, so exciterAir's
  16 kHz roll-off at 32 kHz no longer puts a double pole on the unit
  circle.
- The output delay is declared in data/kernels/idelay.json, and
  omx_idelay.h gains OMX_IDELAY_MAX_MS, the rendered
  OMX_OUTPUT_DELAY_RANGE_MAX.
- No test or tool types a rate list the contract declares: they read the
  contract's lists, and make lint checks it.
- New headers omxdsp/mix/omx_key.h (omx_key and omx_key_build, a
  dynamics slot's key) and omxdsp/mix/omx_src_blend.h (omx_src_blend, the
  switch between a live and a playback source), moved from the console
  engine bit for bit, and omx_meter_level_db in omxdsp/mix/omx_meter.h, a
  level meter's dBFS reading. Golden digests at the nine oracle rates,
  written by the engine's own copies.
- The floor of omx_lin_to_db is declared in
  data/primitives/lin-to-db-floor.json and rendered as
  OMX_LIN_TO_DB_FLOOR_LIN and OMX_LIN_TO_DB_FLOOR_DB (-180 dB); the value
  is the same 1e-9 as before (#177).
- omx_idelay.h declares its ring size, OMX_IDELAY_MAX_RATE and
  OMX_IDELAY_CAP (192001 samples).
- The tests name the nine rates OMX_ORACLE_FULL_RATES and no vendor (#176);
  the chorus and flanger kernel oracles run at all nine (#179).
- make -jN test generates the kernel lists once and runs test-fx one
  target per kernel, side by side; perturb.sh writes its case list into its
  own scratch directory (#153, #163).
- Cost benches for the drive and flanger kernels (make bench-drive, make
  bench-flanger), and one interleaved before/after script for every bench.
- omx-contract-devel >= 2.16.0.

* Sun Oct 18 2026 Pau Aliagas <linuxnow@gmail.com> - 0.23.0-1
- New header omxdsp/mix/omx_bus_stage.h with omx_mix_strip,
  omx_bus_out_gain and omx_bus_out_stage, the console engine's strip and
  bus output stages, bit for bit, with their contracts.
- omxdsp/analysis/omx_hrp_lv2.h gains the calls a plugin face drives the
  live HRP core through: asks and answers, their counters, the block and
  restart helpers. HRP's family and bands controls are declared in data/.
- Delay taps: the read taps move out of struct omx_fx_delay into struct
  omx_fx_delay_taps, read by omx_fx_delay_process_taps;
  omx_fx_delay_process is that call with no taps. omx_fxdelay_tap_gains is
  now omx_fxdelay_tap_legs and takes a non-finite pan as centre. New
  omx_fxdelay_tap_ms gives a tap's time in milliseconds. The delay's output
  does not change.
- The pitch instance runs at the nine rates from 32 to 192 kHz; at 32, 64
  and 128 kHz it used to pass the signal through. At 32 kHz the pre-filter
  corner stays below Nyquist.
- omx_pole_rescale leaves the pole as it is when the reference rate is not
  above 0, as it already did for the running rate.
- omx-contract-devel >= 2.16.0.

* Sat Oct 17 2026 Pau Aliagas <linuxnow@gmail.com> - 0.22.0-1
- The definitions of the kernels and DSP constants this library implements
  now ship with it. They live in data/, one file per kernel and one per
  constant, and install into omx-contract's contract directory as the
  package omx-dsp, with a MANIFEST.json. omx-contract 2.15.0 no longer
  carries them.
- The code reads them through omxdsp/omxdsp_definitions.h, rendered from
  data/ and committed. Every define it holds is the same line omx-contract
  2.14.0's header held. The declared rates and parameter scales still come
  from omx-contract's header, which it includes.
- Each definition names the code that implements it, and where the console
  engine declared it when it was first imported.
- omx-contract-devel >= 2.15.0.

* Fri Oct 16 2026 Pau Aliagas <linuxnow@gmail.com> - 0.21.0-1
- The mix maths the engine used to carry now lives here: the pan laws and
  the LCR downmix centre level (omx_pan_law), a strip's coefficients, its
  split and settled-silence test (omx_mix_coef), the strip's post-fader peak
  reading (omx_meter) and an output route's fill, fold and fold-fill gains
  (omx_route_gain), each with goldens written by the engine's own copies.
- New kernels: omx_mbcomp, a multiband compressor over an LR4 crossover
  tree, and omx_pole_rescale, one home for the reference-rate pole law that
  the delay tone and reverb damping now call.
- The delay has up to four integer read taps on its one ring. The band
  dynamics gain path runs on the libm-free unit pair in 64-sample chunks.
- omxdsp.h includes omx_align.h, and a check proves every public header is
  reached from it or listed. omx_dyn seeds y[n-1] when its slot enters the
  feedback loop.
- The oracles carry more sabotage arms: the tap oracle sees six broken
  kernels, the pole-rescale checks see four broken copies, the multiband
  oracle five, the geq oracle a seventh.

* Fri Oct 16 2026 Pau Aliagas <linuxnow@gmail.com> - 0.20.2-1
- The header documentation states its design notes as plain facts, readable
  without any other document. No code changes: the library and its output
  are the same as 0.20.1's

* Thu Oct 15 2026 Pau Aliagas <linuxnow@gmail.com> - 0.20.1-1
- omx-contract is a dependency floor only: omx-contract-devel >= 2.11.0 and
  omxdsp.pc requires omx-contract >= 2.11.0, with no upper bound. 0.20.0
  declared "< 2.12", which refused any later contract.
- A low-pass with Q below 1/sqrt(2) near Nyquist no longer sits further from
  the analogue prototype than the RBJ cookbook at 44.1 and 48 kHz (up to
  0.18 dB); no golden digest moves (#119)

* Thu Oct 15 2026 Pau Aliagas <linuxnow@gmail.com> - 0.20.0-1
- The live HRP shell (analysis/omx_hrp_lv2.h), the feedback suppressor's
  LV2 face, is now held at every rate the console runs, 32 to 192 kHz, not
  only at 48 kHz: when it asks its worker for analysis, which hop it reads,
  that an idle shell passes audio untouched, that an adopted band cuts
  exactly what it reports, and that bypass walks every band out in even
  steps. Each check has a deliberately broken copy that must fail at all nine
  rates. With this the console engine keeps no HRP or FBS tests of its own:
  they all live here. No API change.

* Thu Oct 15 2026 Pau Aliagas <linuxnow@gmail.com> - 0.19.0-1
- The mix module grows by the rest of the console engine's mix maths, moved
  unchanged and held to the engine's output bit for bit at the nine rates:
  mix/omx_bus_sum.h (one source's contribution to a summing bus, as entries
  of the mix matrix), mix/omx_rta_tap.h (one analyser tap's reading: the mono
  sum, one spectrum and the low zoom), mix/omx_rt_load.h (the real-time load
  meter's measure half), and in mix/omx_meter.h the peak hold and the
  gain-reduction reading's hold and recovery.

* Thu Oct 15 2026 Pau Aliagas <linuxnow@gmail.com> - 0.18.1-1
- The EQ sabotage check for the 0.999 Nyquist hold no longer depends on the
  libm: a peak just under Nyquist makes the held point differ by several dB,
  where 0.18.0 saw a last-bit difference that aarch64 did not have.
- omx_align_fit reads an identical pair as a delay of exactly 0: the anchor's
  three heights are read from the band's bins, not from the transform, whose
  rounding put the peak 5.8e-14 of a sample off lag 0.
- The EQ low-pass near Nyquist above Q 1/sqrt(2) no longer puts a null in its
  passband: the hand-over ends sooner and hands the Nyquist target over to
  the cookbook's zero, so at every top corner and Q of the declared space it
  is no further from the prototype than the cookbook.

* Wed Oct 14 2026 Pau Aliagas <linuxnow@gmail.com> - 0.18.0-1
- analysis/omx_room.h, omx_sweep.h and omx_align_fit.h: OpenMixer's room
  analysis (H1 transfer and coherence, impulse response and early
  reflections, Schroeder RT60, mode finder, mode-EQ proposal), the Farina
  sweep and deconvolution, and Smart Alignment's delay and polarity fit,
  moved from TypeScript; held to closed forms and to a parity table of the
  TypeScript's answers
- The low-pass hands its poles over to the bilinear pair near Nyquist, so
  the passband no longer lifts (#105)
- mix/: the pan law over a speaker layout, strip and fold coefficients, a
  bus's out stage and the meters' measure half, with golden digests (#98)
- omx_wetdry_xfade_block and flush-to-zero on 32-bit ARM, for omx-clap-
  core's hosted stage (omx-clap-core#61)
- The chorus voices read both legs through omx_fdelay_read_pair (#12)
- The align and reverse render oracles and digests run at the nine RME rates
  (#75)
- omx-contract is an installed package taken by pkg-config inside the range
  the packaging declares; nothing is downloaded and there is no pins file
  (#95, #107)
- The drive's hf_rolloff is a DRIVE_HF_ROLLOFFS id (0 off, 1, 2) and its
  corner comes from the contract's omx_drive_hf_rolloffs_value; builds
  against omx-contract >= 2.11.0, < 2.12 (#97)

* Wed Oct 14 2026 Pau Aliagas <linuxnow@gmail.com> - 0.17.0-1
- The gate's key filter: hp_hz and lp_hz in omx_gate_controls and the
  instance's resolve, run in double; tested at the nine RME rates
- omx_drive_instance_resolve takes the contract's oversample control (1, 2
  or 4) and the latency follows the factor
- Builds against omx-contract >= 2.10.1, < 2.11

* Wed Oct 14 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.0-1
- omx_wetdry_mix blends the delay and the reverb, which no longer restate the
  wet/dry pair (#67).
- omx_fdelay_tick_pair ticks two fractional delay lines with one split and one
  kernel; the flanger's two legs use it (#57).
- The interpolated delay's oracle and digests run at the nine RME rates, the
  six earlier digests unchanged (#81).
- dyn: a BELOW slot skips the dB path where its gain is flat (gate open or on
  its floor), at the cost the gate had before (#56).

* Tue Oct 13 2026 Pau Aliagas <linuxnow@gmail.com> - 0.14.0-1
- omx_loudness.h: EBU R 128 loudness as ITU-R BS.1770-4 defines it: the
  K-weighting designed for the rate, momentary, short-term and gated
  integrated loudness, the loudness range of EBU Tech 3342 and the x4
  true peak; tested against EBU Tech 3341 and 3342 signals at the nine
  RME rates

* Tue Oct 13 2026 Pau Aliagas <linuxnow@gmail.com> - 0.13.0-1
- The EQ maths openmixer computes in TypeScript, in C: the bank and
  head filters an EQ runs (omx_eq_bank_design, omx_eq_pass_design), a
  section's complement, the identity test, the analogue width-to-Q law, a
  band's magnitude and the drawn curve with its frequencies and bands
- A parity table of the TypeScript at the nine RME rates holds them to
  it

* Tue Oct 13 2026 Pau Aliagas <linuxnow@gmail.com> - 0.12.1-1
- Tests only: the kernel arms OpenMixer's engine tests held (the LFO,
  the one-pole, the oversampler and the comp's alias gate, the matched EQ
  design, the fractional delay line and its sabotage battery, the band
  dynamics at the nine RME rates) now run in make test. No API change

* Tue Oct 13 2026 Pau Aliagas <linuxnow@gmail.com> - 0.12.0-1
- omx_magnitude.h: the magnitude in dB of a designed section or cascade
  at the frequencies the caller passes, floored for a full null, and a
  band's curve anchors
- omx_eq_bandwidth_q is the one bandwidth-to-Q law, with a golden table
  for its copies

* Tue Oct 13 2026 Pau Aliagas <linuxnow@gmail.com> - 0.11.0-1
- omx_idelay.h: the integer delay line with its click-free re-point, moved
  from the console's route and bus-output delay; its output is unchanged
  bit for bit

* Tue Oct 13 2026 Pau Aliagas <linuxnow@gmail.com> - 0.10.0-1
- Three primitives moved from the OpenMixer engine, unchanged in
  behaviour: the offline sample-rate converter (omx_src.h), the test-
  signal generators (omx_gen.h), and the analyser's complex spectrum and
  half-band decimator, which join the capture ring and spectrum in
  analysis/omx_rta.h. Golden digests at the nine RME rates, written by the
  engine's own copies, hold them bit for bit
- Built against omx-contract 2.6.0, which declares the converter's design
  and the generators' kinds and waveforms; any 2.x from 2.6.0 on

* Mon Oct 12 2026 Pau Aliagas <linuxnow@gmail.com> - 0.6.1-1
- The rotor read its LFO carry before setting it on the first tick; it is
  now cleared at settle
- The pitch, chorus and flanger state inits always set both delay lines
- Builds clean with GCC 13 -Wall -Wextra -Werror

* Mon Oct 12 2026 Pau Aliagas <linuxnow@gmail.com> - 0.6.0-1
- The pitch instance face reports its latency, d_min plus half the window,
  when the mix is 100 %, and 0 below it, where the dry path is on time.
  Outputs are unchanged
- OMX_PITCH_INSTANCE_LATENCY_FRAMES is removed: the latency is the face's
  latency function

* Sun Oct 11 2026 Pau Aliagas <linuxnow@gmail.com> - 0.5.3-1
- The dynamics and band-dynamics states record gr_min_db, the deepest gain
  applied in the last call, in dB; omx_gr_block_db gives a block's reading.
  Outputs are unchanged
- The engine-identity desk check is gone

* Fri Oct 09 2026 Pau Aliagas <linuxnow@gmail.com> - 0.5.2-1
- A trim face, fx/omx_trim_instance.h: the console's input trim, a
  de-zippered gain; its resolve takes the trim kernel's trimDb, clamped
  into TRIM_RANGE
- With the EQ face's pass filters it is the channel strip plugin's input
  stage, bit for bit at every declared rate
- Built against omx-contract 2.3.0; any 2.x from 2.3.0 on

* Fri Oct 09 2026 Pau Aliagas <linuxnow@gmail.com> - 0.5.1-1
- The gate runs the contract's knee range (kneeStartDb, kneeEndDb): a rounded
  corner from the start to the end point around the threshold; a start equal
  to its end is the hard knee, the 0.5.0 gate bit for bit
- The gate face's resolve takes the knee start and end after the range, in
  the contract's order

* Fri Oct 09 2026 Pau Aliagas <linuxnow@gmail.com> - 0.5.0-1
- Built against omx-contract 2.2.0, and requires any 2.x from 2.2.0 on, not
  one exact release: a contract minor keeps every existing define unchanged
- The drive face takes the auto-gain, stereo-link and HF roll-off controls
- A delay instance face that owns its 2 s rings and takes the ping-pong switch
- A stereo EQ instance face taking the EQ's contract controls in order, one
  build per band count (8, 16 or 32 bands)
- The dynamics face is now the comp face (omx_comp_instance.h), taking the
  comp's mix, its kind (comp or limiter, RMS or peak detector) and its
  detector oversampling
- The gate face takes the hold and the hysteresis the kernel now runs
* Fri Oct 09 2026 Pau Aliagas <linuxnow@gmail.com> - 0.4.1-1
- Built against omx-contract 2.1.0

* Fri Oct 09 2026 Pau Aliagas <linuxnow@gmail.com> - 0.4.0-1
- pitch and limiter instance faces own their rings: init takes (instance, rate)
  and allocates nothing (breaking while 0.x: the caller-ring init is gone)

* Fri Oct 09 2026 Pau Aliagas <linuxnow@gmail.com> - 0.3.0-1
- Instance faces for tremolo, phaser, pitch, rotary and limiter (omx-contract 2.0.0)
- transient face: attack_time_ms, sustain_time_ms

* Thu Oct 08 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.0-1
- omx-dsp now builds against omx-contract 1.3.0 and no longer carries its own
  copy of the console's limits. Every limit, travel, default, list and choice
  the kernels read comes from the contract's header
  (`omxcontract/omx_contract_limits.h`, pinned by this tree); the
  library installs and requires `omx-contract-devel` (or
  `libomx-contract-dev`) at exactly that version, and `omxdsp.pc` requires it.
- Breaking, while the library is 0.x: `omxdsp/omx_contract_limits.h` is gone.
  A program that read names from it now includes
  `<omxcontract/omx_contract_limits.h>`, and the console-only names the old
  header carried for the engine (about 460) are not in the contract and are
  not here.
- The kernels' own copies of contract values are gone: the chorus, flanger,
  phaser and reverb ceilings and base delays, the three fractional-delay read
  orders, the ring corrector's default amount, the 31 graphic EQ centres, the
  EQ band types, slopes and pass-filter defaults, and the oracle rate lists.
  Their names stay as definitions of the contract's. No sound changes: every
  golden digest is the one it was.
- An unconnected EQ band port now reads the contract's one default rule for
  the bank (the band's centre and type for its place among the bands) instead
  of a 1 kHz bell.
- The joint EQ band budget is checked by omx-contract itself, so the test that
  restated it is gone.
- `tools/contract-agree.sh`, its gap list and the render check against the
  console are gone with the header they compared. `tools/contract-include.sh`
  finds the contract (an installed package, else the pinned release), and a
  build that cannot find exactly the pinned version stops.

* Thu Oct 08 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.8-1
- Converting a level to decibels calls the system's log10f again, about five
  times faster than the correctly rounded version it replaced. That version,
  omx_log10f, is no longer part of the library: it lives in the tests, which
  use it so every reference output stays exact on any system.
- On glibc older than 2.41 (Debian bookworm) the result can differ from the
  correctly rounded one by up to 2 ulp of a dB value. glibc 2.41 rounds log10f
  correctly.

* Thu Oct 08 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.7-1
- The FFT the console's analyser runs on is now part of the library: the Hann
  window, a complex and a real single-precision transform, and a
  double-precision complex transform with its inverse for room and alignment
  measurements. The single-precision transforms give exactly the console's
  previous output; every transform is checked against a long-double reference.
- The dynamics, balance, rotor and limiter are now tested at all nine rates an
  RME interface runs at, from 32 to 192 kHz, and their reference outputs are
  kept for each of those rates.
- The rotor that drives the rotary speaker has its own test, brought over from
  the console.
- A new check builds the console engine's own copies of these four and
  confirms they give exactly the same output as the library, so the engine can
  switch to the library without a change in sound. Their code is unchanged.
- Two analysis engines arrive from the console, unchanged: the feedback
  detector, which finds a ring growing out of a spectrum and says where to
  notch it, and HRP, which follows the notes an instrument plays, learns how
  its harmonics normally sit and sizes the cuts for the ones that ring. Both
  read a spectrum the caller hands them, allocate nothing and run off the
  audio thread. Include them from `omxdsp/analysis/`.
- Both are tested at all nine sample rates an RME interface offers, from 32 to
  192 kHz, and their output is held bit for bit to what the console computed
  before they moved.

* Wed Oct 07 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.6-1
- The delay effect's instance header and the plugin parameter headers are no
  longer part of the library. They belong to the plugin, and omx-delay now
  carries its own. Nothing else changed.

* Wed Oct 07 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.5-1
- The arm64 and aarch64 packages are published again, for Raspberry Pi OS and
  Fedora on ARM. The library itself is unchanged since 0.1.4.

* Tue Oct 06 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.4-1
- A summing-matrix multiply that mixes many strips into many outputs at once,
  in a dense and a sparse form, and ramps a gain smoothly when it changes in
  the middle of a block.
- One fader law for the whole project: fader position, pan, sends, mute and
  DCA groups resolve to a single gain, so the console, the fader plugin and
  the channel-strip plugin agree.
- A small benchmark for the matrix multiply, at 32, 64 and 97 strips.
- More effects arrive from the console, each checked against a closed-form
  result at every sample rate it supports: limiter, band dynamics, de-esser,
  tremolo and rotary speaker.
- The building blocks of the chorus, drive, flanger, reverb, transient shaper,
  31-band graphic EQ, parametric EQ, gate and compressor are now in the
  library.
- The strip's dynamics and balance code moved over unchanged from the engine.
- The decibel conversion no longer depends on the system's log10f, so it gives
  the same answer on every machine.

* Sun Oct 04 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.3-1
- The half-band filter used by the oversampler runs sixteen outputs at a time,
  with results identical to the loop it replaces.
- A stereo effect can state in one value that both of its inputs are finite
  numbers.
- The thread-sanitizer gate keeps the whole log of a failed run and prints
  every report.

* Fri Oct 02 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.2-1
- The library comes in three builds side by side: the normal one, one with its
  safety checks compiled in, and one for thread-sanitizer runs. Each has its
  own pkg-config file.

* Thu Oct 01 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.1-1
- Parameter clamping gives one defined answer for NaN and for infinity.

* Thu Oct 01 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.0-1
- First package: the DSP building blocks and the delay effect.
