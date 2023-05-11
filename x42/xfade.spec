# Tag: Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    xfade.lv2
Version: 0.3.4
Release: 1%{?dist}
Summary: stereo DJ X-fade plugin
License: GPLv2+
URL:     https://github.com/x42/xfade.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/xfade.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: lv2-devel

%description
xfade.lv2 is an audio-plugin for stereo cross-fading
2 x 2 input channels to 2 output channels.

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
* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.3.4-1
- update to 0.3.4-1

* Sun Nov 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-1
- update to 0.3.3-1

* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.3.2-1
- Initial spec file
