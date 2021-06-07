# spec file for package ChowCentaur
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Tag: Guitar, Overdrive
# Type: Plugin, LV2, VST
# Category: Audio, Effect


Name:    ChowCentaur
Version: 1.4.0
Release: 1%{?dist}
Summary: Digital emulation of the Klon Centaur guitar pedal
License: BSD-3-Clause
URL:     https://github.com/jatinchowdhury18/KlonCentaur

# to generater code archive:
# ./source_chowcentaur.sh <tag>
# ./source_chowcentaur.sh 1.4.0

Source0: KlonCentaur.tar.gz
Source1: source_chowcentaur.sh

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: pkgconfig(gtk+-x11-3.0)
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libcurl-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: xsimd-devel
BuildRequires: lv2-devel
BuildRequires: JUCE
BuildRequires: cmake

%description
The model is constructed using a variety of circuit modelling techniques, 
including nodal analysis, wave digital filters, and recurrent neural networks.

%package -n vst3-%{name}
Summary: Digital emulation of the Klon Centaur guitar pedal (VST3)

%description -n vst3-%{name}
Digital emulation of the Klon Centaur guitar pedal using RNNs, Wave Digital Filters, and more

%package -n lv2-%{name}
Summary: Digital emulation of the Klon Centaur guitar pedal (LV2)

%description -n lv2-%{name}
Digital emulation of the Klon Centaur guitar pedal using RNNs, Wave Digital Filters, and more

%prep
%autosetup -n KlonCentaur

%build
%set_build_flags

%cmake -B cmake-build -DCMAKE_BUILD_TYPE=Release -DRTNEURAL_XSIMD=ON -DCMAKE_PREFIX_PATH=/usr/lib64/juce
touch cmake-build/ChowCentaur/ChowCentaur_artefacts/JuceLibraryCode/AppConfig.h
cmake --build cmake-build %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
install cmake-build/ChowCentaur/ChowCentaur_artefacts/Release/Standalone/* %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_libdir}/vst3
cp -r cmake-build/ChowCentaur/ChowCentaur_artefacts/Release/VST3/*.vst3 %{buildroot}%{_libdir}/vst3/
mkdir -p %{buildroot}%{_libdir}/lv2
cp -r cmake-build/ChowCentaur/ChowCentaur_artefacts/Release/LV2/*.lv2 %{buildroot}%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n vst3-%{name}
%doc README.md
%license LICENSE
%{_libdir}/vst3/

%files -n lv2-%{name}
%doc README.md
%license LICENSE
%{_libdir}/lv2/

%changelog
* Wed May 26 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-1
- update to 1.4.0

* Sun Mar 14 2021 Yann Collette <ycollette.nospam@free.fr> - 1.3.6-1
- update to 1.3.6

* Fri Mar 5 2021 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-1
- update to 1.3.0

* Sun Feb 28 2021 Yann Collette <ycollette.nospam@free.fr> - 1.2.10-1
- update to 1.2.10

* Sat Jan 30 2021 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- Initial spec file
