# Tag: Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    midifilter.lv2
Version: 0.7.1
Release: 1%{?dist}
Summary: LV2 plugins to filter midi events
License: GPLv2+
URL:     https://github.com/x42/midifilter.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/midifilter.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: lv2-devel

%description
LV2 plugins to filter MIDI events.
So far 29 MIDI event filters have been implemented:
 - CC2Note -- translate control-commands to note-on/off messages
 - Channel Filter -- discard messages per channel
 - Channel Map -- map any MIDI-channel to another MIDI-channel
 - Choke Filter -- trigger note-off events, create exclusive note-groups
 - Enforce Scale -- force midi notes on given musical scale
 - Eventblocker -- notch style message filter. Suppress specific messages
 - Keyrange -- discard notes-on/off events outside a given range
 - Keysplit -- change midi-channel number depending on note (and optionally transpose)
 - MapCC -- change one control message into another
 - Mapscale -- flexible 12-tone note map
 - Mapkeychannel -- 12-tone channel map.
 - Chord -- harmonizer - create chords from a single note in a given musical scale
 - Delay -- delay MIDI events with optional randomization
 - Dup -- unisono - duplicate MIDI events from one channel to another
 - Strum -- arpeggio effect intended to simulate strumming a stringed instrument (e.g. guitar)
 - Transpose -- chromatic transpose MIDI notes
 - Legato -- hold a note until the next note arrives
 - NoSensing -- strip MIDI Active-Sensing events
 - NoDup -- MIDI duplicate blocker. Filter out overlapping note on/off and duplicate messages
 - Note2CC -- convert MIDI note-on messages to control change messages
 - Note2PC -- convert MIDI note messages to patch/program change messages
 - NoteToggle -- toggle notes: play a note to turn it on, play it again to turn it off
 - nTabDelay -- repeat notes N times (incl tempo-ramps -- eurotechno hell yeah)
 - Simple 1 Channel Filter -- convenient MIDI channel filter
 - Passthru -- no operation, just pass the MIDI event through (example plugin)
 - Quantize -- live midi event quantization
 - Velocity Randomizer -- randomly change velocity of note-on events
 - ScaleCC -- modify the value (data-byte) of a MIDI control change message
 - Sostenuto -- delay note-off messages, emulate a piano sostenuto pedal
 - Tonal Pedal -- hold active notes when pressing the sustain pedal
 - Velocity Range -- filter MIDI note events according to velocity
 - Velocity Gamma -- modify note velocity curve by a gamma exponent
 - Velocity Scale -- modify note velocity by constant factor and offset

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"
%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%install 

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Sun Nov 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.7.1-1
- update to 0.7.1-1

* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-1
- Initial spec file
