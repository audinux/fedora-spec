# Tag: Live, MIDI, OSC
# Type: Language
# Category: Sequencer, Programming

%global debug_package %{nil}

# Global variables for github repository
%global commit0 d027a414d5ff257b52c613284673933077a53cfa
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: orca-lang
Version: 0.1.0.%{shortcommit0}
Release: 4%{?dist}
Summary: Esoteric programming language and live editor
License: MIT
URL: https://git.sr.ht/~rabbits/orca

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/hundredrabbits/Orca-c/archive/%{commit0}.tar.gz#/orca-%{shortcommit0}.tar.gz
# From https://github.com/hundredrabbits/Orca
Source1: https://github.com/hundredrabbits/Orca/archive/master.zip#/orca-doc.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: alsa-lib-devel
BuildRequires: portmidi-devel
BuildRequires: unzip

%description
Orca is an esoteric programming language and live editor designed to quickly
create procedural sequencers. Every letter of the alphabet is an operation,
lowercase letters execute on *bang*, and uppercase letters execute each frame.

This is the C implementation of the ORCA language and terminal livecoding
environment. It's designed to be power efficient. It can handle large files,
even if your terminal is small.

Orca is not a synthesizer, but a flexible livecoding environment capable of
sending MIDI, OSC, and UDP to your audio/visual interfaces like Ableton,
Renoise, VCV Rack, or SuperCollider.

%prep
%autosetup -n Orca-c-%{commit0}

unzip %{SOURCE1}

sed -i -e 's/add cc_flags -std=c99/add cc_flags -g $CFLAGS -std=c99/g' tool

%build

%set_build_flags

export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`

%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 build/orca %{buildroot}%{_bindir}/%{name}
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
cp -r examples %{buildroot}/%{_datadir}/%{name}/examples
cp -r Orca-main/resources %{buildroot}/%{_datadir}/%{name}/documentation

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*
%{_datadir}/%{name}/

%changelog
* Tue Jun 13 2023 Justin Koh <j@ustink.org> - 0.1.0.d027a414-4
- Rename package to orca-lang

* Sun Oct 09 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1.0.d027a414-3
- update to d027a414d5ff257b52c613284673933077a53cfa

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.0.774d7863-2
- fix debug buid + update to 774d78635745d02f42440e701ae1210ca4197840

* Sat May 9 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.0.3a92c8e3-1
- Initial spec file
