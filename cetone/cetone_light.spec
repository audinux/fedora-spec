# Tag: Audio, Synthesizer
# Type: Plugin, VST3, VST, LV2, CLAP, Standalone
# Category: Audio, Synthesizer

Name: cetone-synth-light
Version: 0.0.1
Release: 1%{?dist}
Summary: Re-implementation of CetoneSynthLight, a light-weight synthesizer by René Jeschke
URL: https://github.com/AnClark/CetoneSynthLight
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-or-later

Vendor:       Audinux
Distribution: Audinux

# ./cetone-source.sh CetoneSynthLight eaffe5f13ae4ae55f1dc1f1aaf285f180bda705c

Source0: CetoneSynthLight.tar.gz
Source1: cetone-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libglvnd-devel

%description
Re-implementation of Cetone Synth, a multifunction synth from Neotec Software

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary: VST2 version of %{name}
License: GPL-3.0-or-later
Requires: %{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep

%autosetup -n CetoneSynthLight

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 -d %{buildroot}%{_libdir}/clap/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/

cp %{__cmake_builddir}/bin/cetone_synth_light %{buildroot}%{_bindir}/
cp %{__cmake_builddir}/bin/cetone_synth_light.clap %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/bin/cetone_synth_light.lv2 %{buildroot}%{_libdir}/lv2/
cp %{__cmake_builddir}/bin/cetone_synth_light-vst2.so %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/bin/cetone_synth_light.vst3 %{buildroot}%{_libdir}/vst3/

%files
%license LICENSE
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Mon May 20 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
