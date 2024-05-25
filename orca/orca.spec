# Tag: Live, MIDI, OSC
# Type: Language
# Category: Sequencer, Programming

%global debug_package %{nil}

# Global variables for github repository
%global commit0 d6bf8e20c534da645813749089ecf3ecec6adbdf
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global commit_doc      34e91f8629d0ddd72fd699402dc598d48cdbe9d7
%global commit_examples da9f09eeab23eb9d61d735042ee3ab81c2598182

Name: orca-lang
Version: 0.1.0.%{shortcommit0}
Release: 5%{?dist}
Summary: Esoteric programming language and live editor
License: MIT
URL: https://git.sr.ht/~rabbits/orca
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://git.sr.ht/~rabbits/orca/archive/%{commit0}.tar.gz#/orca-%{shortcommit0}.tar.gz
Source1: https://git.sr.ht/~rabbits/orca-rack/archive/%{commit_doc}.tar.gz#/orca-rack-master.tar.gz
Source2: https://git.sr.ht/~rabbits/orca-examples/archive/%{commit_examples}.tar.gz#/orca-examples-master.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: alsa-lib-devel
BuildRequires: portmidi-devel

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
%autosetup -n orca-%{commit0}

tar xvfz %{SOURCE1}
tar xvfz %{SOURCE2}

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
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/examples/
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/documentation/
cp -r examples %{buildroot}/%{_datadir}/%{name}/examples/
cp -r orca-examples-%{commit_examples}/* %{buildroot}/%{_datadir}/%{name}/examples
cp -r orca-rack-%{commit_doc}/* %{buildroot}/%{_datadir}/%{name}/documentation

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*
%{_datadir}/%{name}/

%changelog
* Sat May 25 2024 Yann Collette <ycollette.nospam@free.fr> - 0.1.0.d6bf8e20-5
- add some more docs and examples

* Sat May 25 2024 Yann Collette <ycollette.nospam@free.fr> - 0.1.0.d6bf8e20-3
- update to d6bf8e20c534da645813749089ecf3ecec6adbdf

* Tue Jun 13 2023 Justin Koh <j@ustink.org> - 0.1.0.d027a414-4
- Rename package to orca-lang

* Sun Oct 09 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1.0.d027a414-3
- update to d027a414d5ff257b52c613284673933077a53cfa

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.0.774d7863-2
- fix debug buid + update to 774d78635745d02f42440e701ae1210ca4197840

* Sat May 9 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.0.3a92c8e3-1
- Initial spec file
