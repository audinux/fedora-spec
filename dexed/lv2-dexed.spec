# Tag: Synthesizer
# Type: LV2
# Category: Plugin, Synthesizer

%global commit0 32cce1ec397899e27e5932e3f732b3f1bf95de6e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: lv2-dexed
Version: 0.9.2.%{shortcommit0}
Release: 1%{?dist}
Summary: LV2 FM multi plaform/multi format plugin
License: Apache-2.0
URL: https://github.com/dcoredump/dexed.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/dcoredump/dexed.lv2/archive/%{commit0}.zip#/%{name}-%{commit0}.zip

BuildRequires: gcc-c++ make
BuildRequires: lv2-devel
BuildRequires: lvtk

%description
Dexed is a multi platform, multi format plugin synth that is closely
modeled on the Yamaha DX7. Under the hood it uses music-synthesizer-for-android
for the synth engine and JUCE as a plugin wrapper.

The goal of this project is to be a tool/companion for the original DX7. Sound
engine with 'float' value parameters, different waveform à la TX81z would be
great but anything that goes beyond the DX7 should and will be a fork of
this project.
This is to keep the compatibility with the original machine.

Dexed is licensed on the GPL v3. The msfa component (acronym for music
synthesizer for android, see msfa in the source folder) stays on the
Apache 2.0 license to able to collaborate between projects.

%prep
%autosetup -n dexed.lv2-%{commit0}

sed -i -e "/INSTALL_DIR=/d" src/Makefile
sed -i -e "/INSTALL_MYPLUGINS_DIR=/d" src/Makefile

sed -i -e "s|/usr/local/bin/dxsyx|/usr/bin/dxsyx|g" bin/dx7sysex2lv2

%build

%set_build_flags
cd src
%make_build

%install

cd src
%make_install INSTALL_DIR=%{buildroot}/%{_libdir}/lv2/ INSTALL_MYPLUGINS_DIR=%{buildroot}/%{_libdir}/lv2/

cd ..
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/tools/
install -m 755 bin/dx7lv2sounds2preset  %{buildroot}%{_datadir}/%{name}/tools/
install -m 755 bin/dx7sysex2lv2  %{buildroot}%{_datadir}/%{name}/tools/

%files
%doc README.md
%{_libdir}/lv2/*
%{_datadir}/%{name}/tools/*

%changelog
* Tue Jun 13 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.2-1
- Initial build

