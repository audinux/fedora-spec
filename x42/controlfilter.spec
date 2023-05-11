# Tag: Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    controlfilter.lv2
Version: 0.5.1
Release: 1%{?dist}
Summary: LV2 Control Port Parameter Filters -- modular synth blocks
License: GPLv2+
URL:     https://github.com/x42/controlfilter.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/controlfilter.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: lv2-devel

%description
LV2 plugins to filter/process Control Parameters, intended to be used with modular synthesizers, in particular ingen
So far 5 filters have been implemented:
* Linear: out = a * in + b
* Invert: out = 1.0 / in
* Exponential: out = a ^ in
* Base-n Logarithm: out = a * log ( abs (b * in) ) / log (c)
* Low Pass Filter, separate time-constants for rise (attack) and fall (release)

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
* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- update to 0.5.1-1

* Sun Nov 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- Initial spec file
