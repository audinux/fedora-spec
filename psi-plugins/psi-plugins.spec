# Tag: Modular, Jack, Alsa
# Type: Plugin, LV2
# Category: Audio, Synthesizer

# Global variables for github repository
%global commit0 83f318d3c43892af7627e25ef12dc656d6f478a0
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: PSI LV2 Plugins
Name:    psi-plugins-doc
Version: 0.0.1
Release: 4%{?dist}
License: GPL
URL:     https://github.com/ycollet/psi-plugins

Source0: https://github.com/ycollet/psi-plugins/archive/%{commit0}.tar.gz#/psi-plugins-%{shortcommit0}.tar.gz
Patch0:  psi-plugins-lv2ui-descriptor.patch

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: python2
BuildRequires: fltk-devel
BuildRequires: fltk-fluid
BuildRequires: non-ntk-devel
BuildRequires: non-ntk-fluid
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel

%description
psi-plugins is a small collection of LV2 plugins ideal for (but not limited to)
electronic music.

%package -n lv2-midi_gate-psi
Summary: PSI Plugins / Midi Gate LV2 plugin

%description -n lv2-midi_gate-psi
This is a stereo gate MIDI based on the example LV2 midi gate plugin by Dave Robillard

%package -n lv2-midi_rnd-psi
Summary: PSI Plugins / Midi Rnd LV2 plugin

%description -n lv2-midi_rnd-psi
midi_rnd is a simple MIDI random note generator for the inspirationally bereft.

It receives incoming note messages and returns a randomized note of the same 
velocity with the parameters defined by octave range and scale. The generated 
note is produced relative to the incoming key.

An attempt to map Note Off midi messages to previously recevied note on
messages is made but is only reliable for sequential input. As a result some 
NoteOn messages may be left hanging. 

%package -n lv2-sidechain_gate-psi
Summary: PSI Plugins / Sidechain Gate LV2 plugin

%description -n lv2-sidechain_gate-psi
This is a stereo gate with optional sidechain input based on the Gate plugin by Steve Harris. 

%package -n lv2-super_welle
Summary: PSI Plugins / Super Welle LV2 plugin

%description -n lv2-super_welle
super_welle is a 2x16 oscillator virtual analog synthesizer. Originally it 
started out as an experiment in simulating the super saw of the 
Roland JP8000/JP8080 but has since widened is scope. 

%prep
%autosetup -p1 -n psi-plugins-%{commit0}

%build

%set_build_flags

./waf configure --prefix=%{_prefix} --libdir=%{_libdir}
./waf build

%install

./waf -j1 install --destdir=%{buildroot}

cp midi_gate-psi.lv2/README.md      README.midi_gate.md
cp midi_rnd-psi.lv2/README.md       README.midi_rnd.md
cp sidechain_gate-psi.lv2/README.md README.sidechain_gate.md
cp super_welle.lv2/README.md        README.super_welle.md

%files
%doc README.md README.midi_gate.md README.midi_rnd.md README.sidechain_gate.md README.super_welle.md
%license LICENSE

%files -n lv2-midi_gate-psi
%{_libdir}/lv2/midi_gate-psi.lv2/*

%files -n lv2-midi_rnd-psi
%{_libdir}/lv2/midi_rnd-psi.lv2/*

%files -n lv2-sidechain_gate-psi
%{_libdir}/lv2/sidechain_gate-psi.lv2/*

%files -n lv2-super_welle
%{_libdir}/lv2/super_welle-psi.lv2/*

%changelog
* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-4
- fix debug build

* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- fix for Fedora 33

* Wed Nov 6 2019 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- fix for Fedora 31

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 0.0.1-2
- update for Fedora 29

* Thu Nov 2 2017 Yann Collette <ycollette dot nospam at free.fr> 0.0.1-2
- multi-packages

* Thu Nov 2 2017 Yann Collette <ycollette dot nospam at free.fr> 0.0.1-1
- initial release 
