# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Name:    inconcert
Version: 20140109
Release: 1%{?dist}
Summary: Live Tempo Adjustment for the Jack Audio Connection Kit
URL:     https://github.com/llloret/osmid
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

# Usage: ./source-inconcert.sh <tag>
#        ./source-inconcert.sh 5362b3419c924051c599764c4885ce0db0264091

Source0: inconcert.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: qt-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: gtest-devel

%description
It's difficult for a band to use MIDI live. It generally requires
that a MIDI click track be fed to the musicians... and the musicians
must conform or be cast out. If there is an error (like a singer
coming in early or the computer having a hitch), there's generally
no means for recovery — you are dead.

InConcert is a MIDI-controlled application that allows a musician to
control the tempo and synchronization of a MIDI sequence. It features
a tap tempo to adjust the beat (and synchronize the beat) and the
ability to skip beats or insert beats. It works by controlling the
Jack Audio Connection Kit's transport. InConcert depends on Jack and
ALSA, and therefore only runs on Linux. 

%prep
%autosetup -n %{name}

%build
%set_build_flags
export CXXFLAGS="-std=c++11 $CXXFLAGS"
%cmake -DINCONCERT_RUN_UNIT_TESTS=OFF
%cmake_build

%install

%cmake_install

%files
%doc README DEVELOPERS AUTHORS BUGS
%license gpl-2.0.txt gpl-3.0.txt
%{_bindir}/*

%changelog
* Fri Dec 02 2022 Yann Collette <ycollette.nospam@free.fr> - 20140109-1
- Initial spec file
