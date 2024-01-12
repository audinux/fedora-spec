# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Name: jack-link
Version: 0.1.9
Release: 1%{?dist}
Summary: JACK transport timebase bridge to Ableton Link
License: GPL-2.0-only
URL: https://github.com/rncbc/jack_link

Vendor:       Audinux
Distribution: Audinux

# Usage: ./jack-link-source.sh <TAG>
#        ./jack-link-source.sh v0.1.9

Source0: jack_link.tar.gz
Source1: jack-link-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel

%description
jack_link is a JACK transport timebase prototype bridge to Ableton Link.

%prep
%autosetup -n jack_link

%build

%set_build_flags
export CCFLAGS="-fPIC $CXXFLAGS"
export LDFLAGS="-fPIC $LDFLAGS"
%make_build PREFIX=/usr

%install

%make_install PREFIX=/usr

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*

%changelog
* Mon Sep 25 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.9-1
- update to 0.1.9-1

* Wed Jan 25 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.8-1
- initial build.
