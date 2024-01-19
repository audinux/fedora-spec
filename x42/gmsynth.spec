# Tag: Alsa, Jack, Synthesizer, MIDI
# Type: Plugin, LV2
# Category: Audio, Tool, Synthesizer

Name: gmsynth.lv2
Version: 0.5.3
Release: 1%{?dist}
Summary: General MIDI LV2 Synth
License: GPL-2.0-or-later
URL: https://github.com/x42/gmsynth.lv2

Vendor:       Audinux
Distribution: Audinuxgm

Source0: https://github.com/x42/gmsynth.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: glib2-devel

%description
gmsynth.lv2 is a General MIDI Sample Player Plugin

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"
%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%install

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.3-1
- update to 0.5.3-1

* Sun Nov 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- update to 0.5.2-1

* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- Initial spec file
