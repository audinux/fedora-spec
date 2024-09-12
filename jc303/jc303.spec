# Status: active
# Tag: Drum
# Type: Plugin, LV2, VST, VST3
# Category: Sequencer, Sampler, Plugin

Name: jc303
Version: 0.11.1
Release: 2%{?dist}
Summary: A Free Roland TB-303 Plugin
License: GPL-3.0-or-later
URL: https://github.com/midilab/jc303
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/midilab/jc303/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: fftw-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel

%description
A Cmake JUCE port of Robin Schmidt Open303, a Roland TB-303 clone plugin.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n %{name}-%{version}

unzip %{SOURCE1}

mv VST_SDK/VST2_SDK vstsdk2.4

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/JC303_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/JC303_artefacts/VST/*  %{buildroot}/%{_libdir}/vst/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/JC303_artefacts/LV2/*  %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Thu Sep 12 2024 Yann Collette <ycollette.nospam@free.fr> - 0.11.1-2
- update to 0.11.1-2

* Wed Sep 04 2024 Yann Collette <ycollette.nospam@free.fr> - 0.11.0-2
- update to 0.11.0-2

* Fri Apr 19 2024 Yann Collette <ycollette.nospam@free.fr> - 0.10.1-2
- update to 0.10.1-2 - fix for f40

* Mon Jan 22 2024 Yann Collette <ycollette.nospam@free.fr> - 0.10.1-1
- update to 0.10.1-1

* Sun Dec 31 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.2-1
- update to 0.9.2-1

* Mon Sep 18 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.1-1
- Initial spec file
