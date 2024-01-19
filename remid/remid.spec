# Tag: MIDI
# Type: Plugin, LV2, Standalone
# Category: Audio, Synthesizer

Name: remid
Version: 0.3
Release: 1%{?dist}
Summary: A lv2 port of the midi controlled implementation of the SID 6581 chip used in the Commodore 64
License: GPL-2.0-or-later
URL: https://github.com/ssj71/reMID.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ssj71/reMID.lv2/archive/refs/tags/v0.3.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: glib2-devel

%description
A lv2 port of the midi controlled implementation of
the SID 6581 chip used in the Commodore 64

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n reMID.lv2-%{version}

sed -i -e "s|lib/lv2|%{_lib}/lv2|g" CMakeLists.txt
sed -i -e "s|lib/lv2|%{_lib}/lv2|g" src/CMakeLists.txt

%build

%cmake
%cmake_build

%install

%cmake_install

%files
%doc README
%license COPYING
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Tue Jul 19 2022 Yann Collette <ycollette.nospam@free.fr> - 0.3-1
- Initial spec file
