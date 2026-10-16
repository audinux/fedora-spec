# Status: active
# Tag: AI, Effect, Amp Simul
# Type: Plugin, LV2
# Category: Effect

# Global variables for github repository
%global commit0 2209dbf6259c414384bcdefd7929bab77926d8eb
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: mod-midi-merger
Version: 0.1.%{shortcommit0}
Release: 1%{?dist}
Summary: A small Jack-internal client to merge MIDI events from several inputs to one output.
License: ISC
URL: https://github.com/mod-audio/mod-midi-merger
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./modaudio-source.sh <project> <tag>
# ./modaudio-source.sh mod-midi-merger 2209dbf6259c414384bcdefd7929bab77926d8eb

Source0: mod-midi-merger.tar.gz
Source1: modaudio-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)

%description
A small Jack-internal client to merge MIDI events from several inputs to one output.
When a new port is registered at the Jack server, this client will connect to it, if:
* it is a MIDI port with outgoing events
* the name does not start with effect
* if it does not belong to itself
The module can be loaded via:
$ jack_load midi-merger /usr/lib64/jack/mod-midi-merger.so
And unloaded via:
$ jack_unload midi-merger

%prep
%autosetup -n %{name}

sed -i -e "s|DESTINATION \${CMAKE_INSTALL_PREFIX}/lib/jack|DESTINATION \${CMAKE_INSTALL_PREFIX}/%{_lib}/jack|g" CMakeLists.txt

%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install

%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/jack/*

%changelog
* Tue May 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-0dd7c814-1
- Initial build
