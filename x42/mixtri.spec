# Tag: Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    mixtri.lv2
Version: 0.4.10
Release: 1%{?dist}
Summary: Matrix Mixer & Trigger (Pre-Processor for Oscilloscope)
License: GPL-2.0-or-later
URL:     https://github.com/x42/mixtri.lv2

Vendor:       Audinux
Distribution: Audinux

# ./x42-source.sh <project> <tag>
# ./x42-source.sh mixtri.lv2 v0.4.10

Source0: mixtri.lv2.tar.gz
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
BuildRequires: libltc-devel

%description
mixtri.lv2 is a matrix mixer and trigger processor intended
to be used with http://x42.github.io/sisco.lv2/

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
* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.10-1
- update to 0.4.10-1

* Wed Mar 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.9-1
- update to 0.4.9-1

* Sun Nov 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.4.8-1
- update to 0.4.8-1

* Thu Nov 03 2022 Yann Collette <ycollette.nospam@free.fr> - 0.4.7-1
- Initial spec file
