# Global variables for github repository
%global commit0 5f378860bf9a0f6864f1b191377905008d85e587
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    osc2midi
Version: 0.2.5
Release: 1%{?dist}
Summary: OSC2MIDI is a highly configurable OSC to jack MIDI (and back).
URL:     https://github.com/ssj71/OSC2MIDI
License: GPLv2+ and GPLv2 and (GPLv2+ or MIT) and GPLv3+ and MIT and LGPLv2+ and (LGPLv2+ with exceptions) and Copyright only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ssj71/OSC2MIDI/archive/v%{version}.tar.gz#/OSC2MIDI-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel

%description
OSC2MIDI is a highly configurable OSC to jack MIDI (and back). It was designed especially for use on linux desktop
and the open source Android app called "Control (OSC+MIDI)" but was deliberately written to be flexible enough
to be used with any OSC controller or target.

%prep
%autosetup -n OSC2MIDI-%{version}

sed -i -e "s/CMAKE_C_FLAGS \"/CMAKE_C_FLAGS \"-fPIC /g" src/CMakeLists.txt

%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DCMAKE_C_FLAGS=-fPIC \
       -DLIBEXEC_INSTALL_DIR=%{_libexecdir}

%cmake_build

%install

%cmake_install

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Fri Oct 4 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- initial spec file
