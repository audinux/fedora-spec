# Tag: Audio, Convolution
# Type: Plugin, LV2
# Category: Audio, Tool

Name: lv2-ir
Version: 1.3.4
Release: 1%{?dist}
Summary: IR LV2 convolution reverb
License: GPL-2.0-or-later
URL: https://github.com/tomscii/ir.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/tomscii/ir.lv2/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: ir_lv2_fix_build_with_lv2.patch

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: gtk2-devel
BuildRequires: libsndfile-devel
BuildRequires: fftw-devel
BuildRequires: zita-convolver-devel
BuildRequires: libsamplerate-devel

%description
IR is a no-latency/low-latency, realtime, high performance signal convolver
especially for creating reverb effects. Supports impulse responses with 1,
2 or 4 channels, in any soundfile format supported by libsndfile.

%prep
%autosetup -p1 -n ir.lv2-%{version}

sed -i -e "s/-Wall/-Wall \$(CFLAGS)/g" Makefile

%build

%set_build_flags

%make_build

%install

%make_install PREFIX=/usr INSTDIR=%{buildroot}/%{_libdir}/lv2

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Sun Aug 20 2023 Yann Collette <ycollette.nospam@free.fr> - 1.3.4
- Initial development
