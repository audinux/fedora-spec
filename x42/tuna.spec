# Tag: Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    tuna.lv2
Version: 0.6.2
Release: 1%{?dist}
Summary: Musical Instrument Tuner
License: GPLv2+
URL:     https://github.com/x42/tuna.lv2

Vendor:       Audinux
Distribution: Audinux

# ./x42-source.sh <project> <tag>
# ./x42-source.sh tuna.lv2 v0.6.2

Source0: tuna.lv2.tar.gz
Source1: x42-source.sh

BuildRequires: gcc gcc-c++ make
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: fftw-devel
BuildRequires: pango-devel
BuildRequires: cairo-devel

%description
A musical instrument tuner with strobe characteristics in LV2 plugin format.

%prep
%autosetup -n %{name}

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"
%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 fat1_VERSION=%{version} STRIP=true

%install 

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 fat1_VERSION=%{version} STRIP=true

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_libdir}/lv2/*
%{_datadir}/*

%changelog
* Wed Nov 02 2022 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-1
- Initial spec file
