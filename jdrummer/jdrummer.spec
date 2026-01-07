# Status: active
# Tag: Drum
# Type: Plugin, Standalone, VST3
# Category: Audio, Sequencer

Name: jdrummer
Version: 1.5
Release: 1%{?dist}
Summary: An open source drum plugin that acts as an alternative to EZDrummer3
License: GPL-3.0-or-later
URL: https://github.com/jmantra/jdrummer
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/jmantra/jdrummer/archive/refs/tags/Initial.tar.gz#/jdrummer-%{version}.tar.gz

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
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: gtk3-devel

Requires: license-%{name}

%description
A powerful, open-source drum machine VST3 plugin built with the JUCE framework.
JDrummer features SoundFont-based drum kits, a comprehensive groove library
with tempo-synced playback, a composition tool, and an intelligent Groove
Matcher that analyzes audio to find matching drum patterns.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n jdrummer-Initial

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/jdrummer_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 %{__cmake_builddir}/jdrummer_artefacts/Standalone/jdrummer %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Mon Jan 05 2026 Yann Collette <ycollette.nospam@free.fr> - 1.5-1
- update to 1.5-1

* Tue Dec 16 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
