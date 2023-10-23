# Global variables for github repository
%global commit0 1321e5d1ce0d75ef8963bf0f0c9a00218c748bb5
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Tag:
# Type: Presets
# Category: Audio

Name:    zynthian-data
Version: 1.0.0
Release: 7%{?dist}
Summary: A set of LV2 presets
License: GPL-2.0-or-later
URL:     https://github.com/zynthian/zynthian-data

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/zynthian/zynthian-data/archive/%{commit0}.tar.gz#/zynthian-data-%{shortcommit0}.tar.gz

BuildArch: noarch

%description
A set of LV2 presets for various plugins:
- DISTRho
- synthv1
- padthv1
- Surge
- Vitalium
- Wolpertinger
- RaffoSynth
- Dexed
- Odin 2

%package distrho
Summary:  Presets for DISTRHO plugins
Requires: DISTRHO-Ports

%description distrho
Presets for DISTRHO plugins

%package synthv1
Summary:  Presets for synthv1 plugin
Requires: lv2-synthv1

%description synthv1
Presets for synthv1 LV2 plugin

%package padthv1
Summary:  Presets for padthv1 plugin
Requires: lv2-padthv1

%description padthv1
Presets for padthv1 LV2 plugin

%package surge
Summary:  Presets for Surge plugin

%description surge
Presets for Surge LV2 plugin

%package vitalium
Summary:  Presets for Vitalium plugin
Requires: DISTRHO-Ports

%description vitalium
Presets for Vitalium LV2 plugin

%package wolpertinger
Summary:  Presets for Wolpertinger plugin
Requires: DISTRHO-Ports

%description wolpertinger
Presets for Wolpertinger LV2 plugin

%package raffosynth
Summary:  Presets for RaffoSynth plugin
Requires: lv2-raffosynth

%description raffosynth
Presets for RaffoSynth LV2 plugin

%package dexed
Summary:  Presets for Dexed plugin
Requires: lv2-dexed

%description dexed
Presets for Dexed LV2 plugin

%package odin2
Summary:  Presets for Odin2 plugin

%description odin2
Presets for Odin2 LV2 / VST3 plugin

%prep
%autosetup -n %{name}-%{commit0}

%build

%install

mkdir -p %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/[oO]bxd*      %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/VEX*          %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/[vV]ex*       %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/synthv1*      %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/padthv1*      %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/Surge*        %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/Vitalium*     %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/Wolpertinger* %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/Raffo_Synth*  %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/dexed*        %{buildroot}/usr/%{_lib}/lv2/
cp -r presets/lv2/Odin2*        %{buildroot}/usr/%{_lib}/lv2/

%files distrho
%{_libdir}/lv2/VEX*
%{_libdir}/lv2/[vV]ex*
%{_libdir}/lv2/[oO]bxd*

%files synthv1
%{_libdir}/lv2/synthv1*

%files padthv1
%{_libdir}/lv2/padthv1*

%files surge
%{_libdir}/lv2/Surge*

%files vitalium
%{_libdir}/lv2/Vitalium*

%files wolpertinger
%{_libdir}/lv2/Wolpertinger*

%files raffosynth
%{_libdir}/lv2/Raffo_Synth*

%files dexed
%{_libdir}/lv2/dexed*

%files odin2
%{_libdir}/lv2/Odin2*

%changelog
* Wed Jan 26 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-7
- update to 1.0.0-7 - 1321e5d1ce0d75ef8963bf0f0c9a00218c748bb5

* Wed Jan 26 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-6
- update to 1.0.0-6

* Mon Mar 22 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-5
- update to 1.0.0-5

* Sun Aug 9 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-4
- update to 1.0.0-4

* Mon Mar 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-3
- fix requires

* Mon Mar 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- Add padthv1 presets

* Sun Mar 15 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
