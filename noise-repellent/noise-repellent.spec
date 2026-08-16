# Status: active
# Tag: Gate
# Type: Plugin, LV2, VST3
# Category: Audio, Effect
# LastSourceUpdate: 2020

Name: noise-repellent
Version: 0.3.2
Release: 5%{?dist}
Summary: A lv2 plug-in for broadband noise reduction.
License: GPL-2.0-or-later
URL: https://github.com/lucianodato/noise-repellent
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/lucianodato/noise-repellent/archive/refs/tags/v%{version}.tar.gz#/noise-repellent-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: alsa-lib-devel
BuildRequires: cairo-devel
BuildRequires: fftw-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gtk3-devel
BuildRequires: libX11-devel
BuildRequires: libXcursor-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libcurl-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: pkgconfig(jack)
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: chrpath

%description
Features
* Spectral gating and spectral subtraction suppression rule
* Adaptive and manual noise thresholds estimation
* Adjustable noise floor
* Adjustable offset of thresholds to perform over-subtraction
* Time smoothing and a masking estimation to reduce artifacts
* Basic onset detector to avoid transients suppression
* Whitening of the noise floor to mask artifacts and to recover higher frequencies
* Option to listen to the residual signal
* Soft bypass
* Noise profile saved with the session

Limitations
* The plug-in will introduce latency so it's not appropriate to be used while recording (23 ms for 44.1 kHz)
* It was developed to be used with Ardour however it is known to work with other hosts

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-2.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-2.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-2.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n noise-repellent-%{version}

sed -i -e "s|PRODUCT_NAME \"Noise Repellent\"|PRODUCT_NAME \"Noise_Repellent\"|g" CMakeLists.txt
%build

%cmake -DUSE_SYSTEM_FFTW=ON \
       -DUSE_SYSTEM_FREETYPE=ON \
       -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/NoiseRepellent_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/NoiseRepellent_artefacts/LV2/*  %{buildroot}/%{_libdir}/lv2/

# Cleanup rpath
chrpath --delete `find %{buildroot}/usr/%{_lib}/vst3/ -name "*.so"`
chrpath --delete `find %{buildroot}/usr/%{_lib}/lv2/ -name "*.so"`

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sun Aug 16 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.2-5
- update to 0.3.2-5

* Sun Aug 09 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-5
- update to 0.3.1-5

* Sun Aug 02 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-5
- update to 0.3.0-5

* Sat Jan 17 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.5-5
- update to 0.2.5-5

* Wed Jan 14 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.4-5
- update to 0.2.4-5

* Tue Mar 07 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.3-5
- update to 0.2.3-5 - fixes

* Fri May 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.3-4
- update to 0.2.3-4

* Sun May 15 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-4
- update to 0.2.2-4

* Sun Apr 24 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.1-4
- update to 0.2.1-4  - obsoletes noie-repellent in favor of lv2-noise-repellent

* Sun Apr 24 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.1-3
- update to 0.2.1-3

* Sat Apr 23 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-3
- update to 0.2.0-3

* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.5-3
- update to 0.1.5-3 - fix debug build

* Mon Jan 6 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.5-2
- update to 0.1.5-2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.4-2
- update for Fedora 29

* Mon May 14 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.4-2
- update to latest version + meson build

* Tue Nov 28 2017 Yann Collette <ycollette.nospam@free.fr> - 0.1.4-1
- Initial build
