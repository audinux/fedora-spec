# Tag: Emulator
# Type: Plugin, LV2
# Category: Audio, Synthesizer
# Global variables for github repository

%global commit0 a2d43931ae58561fff2c22d0885f54ebebab36d0
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: raffosynth
Version: 0.1.0
Release: 1%{?dist}
Summary: This is a digital emulator of a minimoog synthesizer, built as an LV2 audio plugin for Linux.
License: GPL-3.0-or-later
URL: https://github.com/nicoroulet/moog

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/nicoroulet/moog/archive/%{commit0}.tar.gz#/moog-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: lv2-c++-tools-devel

%description
This is a digital emulator of a minimoog synthesizer, built as an LV2 audio plugin for Linux.

%package -n lv2-%{name}
Summary: This is a digital emulator of a minimoog synthesizer, built as an LV2 audio plugin for Linux.

%description -n lv2-%{name}
This is a digital emulator of a minimoog synthesizer, built as an LV2 audio plugin for Linux.

%prep
%autosetup -n RaffoSynth-%{commit0}

sed -i -e "s/FLAGS = -O3 -std=c++11/FLAGS = -std=c++11 \$(SPEC_CFLAGS)/g" Makefile
sed -i -e "s/CFLAGS = -std=c99 -O3/CFLAGS = -std=c99 \$(SPEC_CFLAGS)/g" Makefile

%build

%set_build_flags

%make_build INSTALL_DIR=%{buildroot}/usr/%{_lib}/lv2/ SPEC_CFLAGS="%{build_cflags} -fPIC"

%install

%make_install INSTALL_DIR=%{buildroot}/usr/%{_lib}/lv2/

%files -n lv2-%{name}
%doc README.md
%license LICENSE.md
%{_libdir}/lv2/*

%changelog
* Tue Oct 20 2020 Yann Collette <ycollette dot nospam at free dot fr> - 0.1.0-2
- fix debug build

* Tue Apr 16 2019 Yann Collette <ycollette dot nospam at free dot fr> - 0.1.0-1
- Initial version of the spec file

