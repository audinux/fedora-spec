# Tag: Effect
# Type: Plugin, LV2
# Category: Effect

Name: vocproc
Version: 0.2.1
Release: 1%{?dist}
Summary: VocProc is a LV2 plugin for pitch shifting (with or without formant correction), vocoding, automatic pitch correction and harmonizing of singing voice.
License: GPL-2.0-or-later
URL: https://hyperglitch.com/dev/VocProc

Vendor:       Audinux
Distribution: Audinux

Source0: https://hyperglitch.com/files/vocproc/vocproc-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: lv2-c++-tools-devel

%description
VocProc is a LV2 plugin for pitch shifting (with or without formant correction), vocoding, automatic pitch correction and harmonizing of singing voice.

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n %{name}.lv2

sed -i -e "s|\$(DESTDIR)/usr/lib/lv2|\$(DESTDIR)/usr/%{_lib}/lv2|g" Makefile

%build

%set_build_flags

%make_build -j1

%install

%make_install

%files -n lv2-%{name}
%doc README
%license COPYING
%{_libdir}/lv2/*

%changelog
* Fri Nov 06 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
