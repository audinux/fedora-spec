# Global variables for github repository
%global commit0 076a23dd0084519e05981588f886c5d7d8a47e5e
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Tag: Presets
# Type: Presets
# Category: Audio

Name:    zynthian-data
Version: 1.0.0
Release: 6%{?dist}
Summary: A set of LV2 presets for DISTRHO
License: GPLv2+
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

%package distrho
Summary:  Presets for DISTRHO plugins
Group:    Applications/Multimedia
Requires: DISTRHO-Ports

%description distrho
Presets for DISTRHO plugins

%package synthv1
Summary:  Presets for synthv1 plugin
Group:    Applications/Multimedia
Requires: lv2-synthv1

%description synthv1
Presets for synthv1 LV2 plugin

%package padthv1
Summary:  Presets for padthv1 plugin
Group:    Applications/Multimedia
Requires: lv2-padthv1

%description padthv1
Presets for padthv1 LV2 plugin

%package surge
Summary:  Presets for Surge plugin
Group:    Applications/Multimedia
Requires: lv2-surge

%description surge
Presets for Surge LV2 plugin

%package vitalium
Summary:  Presets for Vitalium plugin
Group:    Applications/Multimedia
Requires: DISTRHO-Ports

%description vitalium
Presets for Vitalium LV2 plugin

%package wolpertinger
Summary:  Presets for Wolpertinger plugin
Group:    Applications/Multimedia
Requires: DISTRHO-Ports

%description wolpertinger
Presets for Wolpertinger LV2 plugin

%package raffosynth
Summary:  Presets for RaffoSynth plugin
Group:    Applications/Multimedia
Requires: lv2-raffosynth

%description raffosynth
Presets for RaffoSynth LV2 plugin

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

%changelog
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
