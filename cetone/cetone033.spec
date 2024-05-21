# Tag: Audio, Synthesizer
# Type: Plugin, VST3, VST, LV2, CLAP, Standalone
# Category: Audio, Synthesizer

Name: cetone033-synth
Version: 0.0.1
Release: 1%{?dist}
Summary: Re-implementation of Cetone033, a chiptune-style synthesizer by René Jeschke
URL: https://github.com/AnClark/Cetone033
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-or-later

Vendor:       Audinux
Distribution: Audinux

# ./cetone-source.sh Cetone033 bb05f7d73a48bd51b1abcb07e8230b5f5664eef9

Source0: Cetone033.tar.gz
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
Cetone033 is a analogue-style bassline synthesizer by Neotec Software.
Though it has been designed for basslines, it's also a chiptune style
synthesizer. Originally written by René Jeschke.

Sadly, Cetone Synth series had been discontinued for more than 12 years
(since 2012), and it only supported VST 2.4. Original project is here.

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

%autosetup -n Cetone033

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 -d %{buildroot}%{_libdir}/clap/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/

cp %{__cmake_builddir}/bin/cetone033 %{buildroot}%{_bindir}/
cp %{__cmake_builddir}/bin/cetone033.clap %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/bin/cetone033.lv2 %{buildroot}%{_libdir}/lv2/
cp %{__cmake_builddir}/bin/cetone033-vst2.so %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/bin/cetone033.vst3 %{buildroot}%{_libdir}/vst3/

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
