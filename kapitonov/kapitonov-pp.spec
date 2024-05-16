# Tag: Guitar, Jack, Overdrive, Amp Simul, Cabinet, Gate, Octaver
# Type: Plugin, LV2
# Category: Audio, Effect

# Global variables for github repository
%global commit0 828dcf7ede9260da6d65ab6896d99d694f7f12af
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: kpp
Version: 1.2.1
Release: 2%{?dist}
Summary: Kapitonov Plugins Pack for guitar
URL: https://github.com/olegkapitonov/Kapitonov-Plugins-Pack
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/olegkapitonov/Kapitonov-Plugins-Pack/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: faust
BuildRequires: meson
BuildRequires: pkgconfig(jack)
BuildRequires: lv2-devel
BuildRequires: ladspa-devel
BuildRequires: libxcb-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: cairo-devel
BuildRequires: zita-resampler-devel
BuildRequires: zita-convolver-devel
BuildRequires: boost-devel
BuildRequires: faust-osclib-devel
BuildRequires: fftw-devel

%description
A set of plugins for guitar sound processing

%package -n lv2-kpp-plugins
Summary: A set of plugins for guitar sound processing - LV2 version
License:GPL-2.0-or-later

%description -n lv2-kpp-plugins
Kapitonov plugins pack.
A set of plugins for guitar sound processing - LV2 version

%package -n ladspa-kpp-plugins
Summary: A set of plugins for guitar sound processing - LADSPA version
License:GPL-2.0-or-later

%description -n ladspa-kpp-plugins
Kapitonov plugins pack.
A set of plugins for guitar sound processing - LADSPA version

%prep
%autosetup -n Kapitonov-Plugins-Pack-%{commit0}

%build

%set_build_flags
%meson -Dlv2dir=%{_lib}/lv2 -Dladspadir=%{_lib}/ladspa
%meson_build

%install

%meson_install

%files -n ladspa-kpp-plugins
%{_libdir}/ladspa/*

%files -n lv2-kpp-plugins
%{_libdir}/lv2/*

%files
%doc README.md guide.md guide_ru.md
%license LICENSE.txt

%changelog
* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-2
- fix debug build

* Wed May 27 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-1
- update to 1.2.1-1

* Mon Jan 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- initial release
