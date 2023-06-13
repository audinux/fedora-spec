# Global variables for github repository
%global commit0 d56812e8d99d8ce2753deb6d631190c9a1223423
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    tunefish
Version: 4.2.0.%{shortcommit0}
Release: 2%{?dist}
Summary: Tunefish virtual analog synthesizer - additive wavetable-based synthesizer VST plugin (git version)
License: GPL-3.0-only
URL:     https://www.tunefish-synth.com/

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/paynebc/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: Makefile-tunefish
Patch0: tunefish_juce-pixel.patch
Patch1: tunefish-aarch64.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: libX11-devel
BuildRequires: mesa-libGL-devel
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: libXinerama-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: simde-devel

%description
Tunefish is a very tiny virtual analog synthesizer.
It is developed to fit into about 10kb of compressed machine code
while still producing an audio quality that can compete with
commercial synthesizers. 

%prep
%setup -n %{name}-%{commit0}

%patch0 -p1
%ifarch aarch64
%patch1 -p1
%endif

cp %{SOURCE1} src/tunefish4/Builds/LinuxMakefile/Makefile

%build

%set_build_flags

cd src/tunefish4/Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true V=1

%install 

cd src/tunefish4/Builds/LinuxMakefile

install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 build/*.so %{buildroot}/%{_libdir}/vst/

install -m 755 -d %{buildroot}%{_libdir}/vst/tf4programs
install -m 644 ../../../../patches/tf4programs/* %{buildroot}/%{_libdir}/vst/tf4programs

%files
%doc README.md
%license COPYING
%{_libdir}/*

%changelog
* Sun Jan 17 2021 Yann Collette <ycollette.nospam@free.fr> - 4.2.0.d56812e8-2
- update to 4.2.0-2

* Thu Oct 22 2020 Yann Collette <ycollette.nospam@free.fr> - 4.1.0.a199cb02-2
- fix debug build

* Sun May 17 2020 Yann Collette <ycollette.nospam@free.fr> - 4.1.0.a199cb02-1
- Initial spec file
