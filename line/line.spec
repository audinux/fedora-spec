# Tag: Tracker, Jack, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name: line
Version: 0.4.19
Release: 1%{?dist}
Summary: tiny command-line midi sequencer and language for live coding
License: MIT
URL: https://github.com/pd3v/line

Vendor:       Audinux
Distribution: Audinux

# Usage: ./line-source.sh <TAG>
#        ./line-source.sh v0.4.19

Source0: line.tar.gz
Source1: line_CMakeLists.txt
Source2: line-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: readline-devel
BuildRequires: rtaudio-devel
BuildRequires: rtmidi-devel
BuildRequires: lua-devel
BuildRequires: opus-devel
BuildRequires: libsamplerate-devel

%description
Tiny command-line midi sequencer for live coding.

%prep
%autosetup -n %{name}

cp %{SOURCE1} CMakeLists.txt

%build

%cmake -DRTMIDI_API_JACK=ON
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp %{__cmake_builddir}/line %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
* Sun Mar 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.19-1
- initial spec file
