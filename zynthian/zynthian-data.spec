# Status: active
# Tag: Presets
# Type: Presets
# Category: Audio

# Global variables for github repository
%global commit0 ddfa009f7ff55c455c7a07d0349f645ee8219354
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: zynthian-data
Version: 1.0.0
Release: 8%{?dist}
Summary: A set of LV2 presets
License: GPL-2.0-or-later
URL: https://github.com/zynthian/zynthian-data
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/zynthian/zynthian-data/archive/%{commit0}.tar.gz#/zynthian-data-%{shortcommit0}.tar.gz

BuildArch: noarch

%description
A set of LV2 presets for various plugins:
- DISTRho
- synthv1
- padthv1
- Vitalium
- Wolpertinger
- RaffoSynth
- Dexed
- Odin 2
- Helm
- Dragonfly
- Custom (OS-251, argotlunar2, mod-mda-DX10, mod-mda-JX10, mod-mda-TestTone)

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

%package dragonfly
Summary:  Presets for Dragonfly plugin
Requires: lv2-dragonfly

%description dragonfly
Presets for Dragonfly LV2 plugin

%package helm
Summary:  Presets for Helm plugin

%description helm
Presets for Helm LV2 plugin

%package custom
Summary:  Presets for Custom plugin

%description custom
Presets for Custom LV2 plugin

%prep
%autosetup -n %{name}-%{commit0}

%build

%install

mkdir -p %{buildroot}/%{_libdir}/lv2/
cp -r presets/lv2/[oO]bxd*      %{buildroot}/%{_libdir}/lv2/
cp -r presets/lv2/VEX*          %{buildroot}/%{_libdir}/lv2/
cp -r presets/lv2/[vV]ex*       %{buildroot}/%{_libdir}/lv2/
cp -r presets/lv2/synthv1*      %{buildroot}/%{_libdir}/lv2/
cp -r presets/lv2/padthv1*      %{buildroot}/%{_libdir}/lv2/
cp -r presets/lv2/Vitalium*     %{buildroot}/%{_libdir}/lv2/
cp -r presets/lv2/Wolpertinger* %{buildroot}/%{_libdir}/lv2/
cp -r presets/lv2/Raffo_Synth*  %{buildroot}/%{_libdir}/lv2/
cp -r presets/lv2/dexed*        %{buildroot}/%{_libdir}/lv2/
cp -r presets/lv2/Odin2*        %{buildroot}/%{_libdir}/lv2/
cp -r presets/lv2/Dragonfly*    %{buildroot}/%{_libdir}/lv2/

cp -r lv2-custom/Obxd.lv2       %{buildroot}/%{_libdir}/lv2/
cp -r lv2-custom/dexed.lv2      %{buildroot}/%{_libdir}/lv2/
cp -r lv2-custom/raffo.lv2      %{buildroot}/%{_libdir}/lv2/
cp -r lv2-custom/TAL-NoiseMaker.lv2 %{buildroot}/%{_libdir}/lv2/
cp -r lv2-custom/Helm.lv2       %{buildroot}/%{_libdir}/lv2/

cp -r lv2-custom/OS-251.lv2     %{buildroot}/%{_libdir}/lv2/
cp -r lv2-custom/argotlunar2.lv2 %{buildroot}/%{_libdir}/lv2/
cp -r lv2-custom/mod-mda-DX10.lv2 %{buildroot}/%{_libdir}/lv2/
cp -r lv2-custom/mod-mda-JX10.lv2 %{buildroot}/%{_libdir}/lv2/
cp -r lv2-custom/mod-mda-TestTone.lv2 %{buildroot}/%{_libdir}/lv2/

%files distrho
%{_libdir}/lv2/VEX*
%{_libdir}/lv2/[vV]ex*
%{_libdir}/lv2/[oO]bxd*
%{_libdir}/lv2/TAL*

%files synthv1
%{_libdir}/lv2/synthv1*

%files helm
%{_libdir}/lv2/Helm*

%files padthv1
%{_libdir}/lv2/padthv1*

%files vitalium
%{_libdir}/lv2/Vitalium*

%files wolpertinger
%{_libdir}/lv2/Wolpertinger*

%files raffosynth
%{_libdir}/lv2/Raffo_Synth*
%{_libdir}/lv2/raffo*

%files dexed
%{_libdir}/lv2/dexed*

%files odin2
%{_libdir}/lv2/Odin2*

%files dragonfly
%{_libdir}/lv2/Dragonfly*

%files custom
%{_libdir}/lv2/OS-251.lv2
%{_libdir}/lv2/argotlunar2.lv2
%{_libdir}/lv2/mod-mda-DX10.lv2
%{_libdir}/lv2/mod-mda-JX10.lv2
%{_libdir}/lv2/mod-mda-TestTone.lv2

%changelog
* Sat Nov 02 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-8
- update to 1.0.0-8

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
