# Tag: Effect, Reverb
# Type: Plugin, LV2
# Category: Audio, Effect

%global commit0 898cadc8b406c9b39de244370c597b7e719c2c73

Name: roboverb
Version: 1.1.0
Release: 1%{?dist}
Summary: A reverberation plugin
License: GPL-3.0-or-later
URL: https://github.com/kushview/roboverb

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeload.github.com/kushview/roboverb/zip/%{commit0}#/%{name}-%{commit0}.zip

BuildRequires: gcc gcc-c++
BuildRequires: meson
BuildRequires: git
BuildRequires: lilv-devel
BuildRequires: lv2-devel
BuildRequires: suil-devel
BuildRequires: zix-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: libXext-devel
BuildRequires: libX11-devel
BuildRequires: libglvnd-devel
BuildRequires: boost-devel

%description
Robotic reverb at your fingertips

%prep
%autosetup -n %{name}-%{commit0}

%build

%meson --wrap-mode=nofallback --force-fallback-for "lvtk,pugl"
%meson_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra %{_vpath_builddir}/roboverb.lv2 %{buildroot}/%{_libdir}/lv2/
rm -rf %{buildroot}/%{_libdir}/lv2/roboverb.lv2/*.p

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/lv2/*

%changelog
* Wed Jan 24 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- Initial version
