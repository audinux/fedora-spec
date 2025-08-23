# Status: active
# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Distortion

%global commit0 b456ddc08ac4098078b0604e69febc863beeada6

Name: bassman-preamp
Version: 0.5.0
Release: 2%{?dist}
Summary: VST3 audio plugin for emulating a guitar amplifier
License: GPL-3.0-or-later
URL: https://github.com/flubber2077/Open-Source-Bassman-Preamp
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/flubber2077/Open-Source-Bassman-Preamp/archive/%{commit0}.zip#/%{name}-%{version}.zip
Source1: Builds.zip

BuildRequires: gcc gcc-c++
BuildRequires: git
BuildRequires: unzip
BuildRequires: JUCE61
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

Requires: license-%{name}

%description
An open source emulation project of the 5F6-A revision of the
Fender Bassman preamp. A fork of the more ambitious project of
emulating the Versatone Pan-O-Flex. Built to better understand
C++, real-time DSP, JUCE, GUI, and Object Oriented Programming.

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
%autosetup -n Open-Source-Bassman-Preamp-%{commit0}

unzip %{SOURCE1}

%build

%set_build_flags

export CXXFLAGS="`pkg-config --cflags gtk+-3.0` -DJUCE_WEB_BROWSER=0 -include utility $CXXFLAGS"

cd Builds/LinuxMakefile

%make_build

%install

cd Builds/LinuxMakefile

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra build/Bassman_Preamp.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 build/Bassman_Preamp %{buildroot}%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sat Aug 23 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-2
- update to 0.5.9-2 - remove unused dep

* Wed Jul 31 2024 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- Initial spec file
