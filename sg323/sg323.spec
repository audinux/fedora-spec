# Tag: Effect, Reverb
# Type: Plugin, VST3, CLAP
# Category: Audio, Effect

Name: sg-323
Version: 0.6.3
Release: 1%{?dist}
Summary: Ursa Major Stargate 323
License: GPL-3.0-only
URL: https://github.com/greyboxaudio/SG-323

Vendor:       Audinux
Distribution: Audinux

# Usage: ./sg323-source.sh <TAG>
#        ./sg323-source.sh 0.6.3

Source0: SG-323.tar.gz
Source1: sg323-source.sh

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
BuildRequires: webkit2gtk3-devel

%description
This plugin is an authentic emulation of my Ursa Major Stargate 323 Reverb.
It is based on over 2 years of work, which included a detailed analysis of
the original circuit logic and filters, as well as the actual eprom data.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-only
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-3.0-only
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n SG-323

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/SG323_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/SG323_artefacts/CLAP/* %{buildroot}/%{_libdir}/clap/

%files
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Fri Jan 26 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- Initial spec file
