# Status: active
# Tag: Tracker, Jack, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name: line
Version: 0.6.1
Release: 1%{?dist}
Summary: tiny command-line midi sequencer and language for live coding
License: MIT
URL: https://github.com/pd3v/line
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./line-source.sh <TAG>
#        ./line-source.sh v0.6.1

Source0: line.tar.gz
Source1: line-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: libatomic
BuildRequires: chrpath
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

sed -i -e "s|std::string parserFile = \"../lineparser.lua\";|std::string parserFile = \"/usr/share/line/lua/lineparser.lua\";|g" line.cpp

%build

%set_build_flags

export LDFLAGS="`pkg-config --libs jack` $LDFLAGS"

%cmake -DRTMIDI_API_JACK=ON \
       -DRTMIDI_API_ALSA=ON

%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp %{__cmake_builddir}/line %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/line/doc/
cp "line's manual.pdf" %{buildroot}/%{_datadir}/line/doc/

install -m 755 -d %{buildroot}/%{_datadir}/line/lua/
cp lineparser.lua %{buildroot}/%{_datadir}/line/lua/

chrpath --delete %{buildroot}/%{_bindir}/line

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/line/doc/*
%{_datadir}/line/lua/lineparser.lua

%changelog
* Mon Jul 29 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.7.4-1
- update to 0.6.7.4-1

* Fri Jul 19 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.5-1
- update to 0.6.5-1

* Thu Jul 18 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.4-1
- update to 0.6.4-1

* Sat May 25 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-1
- update to 0.6.2-1

* Sun Mar 03 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-1
- update to 0.6.1-1

* Sun Mar 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.19-1
- initial spec file
