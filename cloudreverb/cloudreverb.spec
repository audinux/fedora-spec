# Status: active
# Tag: Effect, Reverb
# Type: Plugin, Standalone, VST3, LV2
# Category: Audio, Effect

Name: cloudreverb
Version: 0.4
Release: 2%{?dist}
Summary: Algorithmic reverb plugin based on CloudSeed
License: MIT
URL: https://github.com/xunil-cloud/CloudReverb
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./cloudreverb-source.sh <TAG>
#        ./cloudreverb-source.sh v0.4

Source0: CloudReverb.tar.gz
Source1: cloudreverb-source.sh

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
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: patchelf

Requires: license-%{name}

%description
This is an audio plugin for algorithmic reverb. The algorithm is
borrowed from CloudSeed VST by Valdemar Erlingsson.

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: MIT
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: MIT
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n license-%{name}
Summary: License and documentation for %{name}
License: MIT

%description -n license-%{name}
License and documentation for %{name}

%prep
%autosetup -n CloudReverb

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/CloudReverb_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/CloudReverb_artefacts/LV2/*  %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/CloudReverb_artefacts/Standalone/*  %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_libdir}/cloudreverb/
cp %{__cmake_builddir}/audio_engine/libaudio_engine.so %{buildroot}/%{_libdir}/cloudreverb/

patchelf --set-rpath '$ORIGIN/../%{_lib}/cloudreverb/' %{buildroot}/%{_bindir}/CloudReverb
patchelf --set-rpath '$ORIGIN/../../cloudreverb/' `find %{buildroot}/%{_libdir}/lv2/ -name "*.so"`
patchelf --set-rpath '$ORIGIN/../../../../cloudreverb/' `find %{buildroot}/%{_libdir}/vst3/ -name "*.so"`

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE
%{_libdir}/cloudreverb/libaudio_engine.so

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Tue Nov 25 2025 Yann Collette <ycollette.nospam@free.fr> - 0.4-2
- update to 0.4-2

* Sat Sep 20 2025 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-2
- update to 0.3.1-2

* Sat Jan 04 2025 Yann Collette <ycollette.nospam@free.fr> - 0.3-2
- update to 0.3-2 - fix rpath modification

* Wed Nov 13 2024 Yann Collette <ycollette.nospam@free.fr> - 0.2-1
- Initial spec file
