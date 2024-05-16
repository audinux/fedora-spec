# Tag: Audio, Effect
# Type: Plugin, VST3
# Category: Effect

Name:    rotor
Version: 1.0.0
Release: 1%{?dist}
Summary: Modern ring modulation effect plugin
License: GPL-3.0-or-later
URL:     https://github.com/blackboxdsp/rotor
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/blackboxdsp/rotor/archive/refs/heads/develop.zip#/%{name}-%{version}.zip
Source1: https://github.com/juce-framework/JUCE/archive/refs/tags/6.0.8.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel

%description
Rotor is a variable waveform ring modulation plugin targeting VST3 and
AU for OS X and Windows platforms.
It uses wavetable synthesis to generate various simple waveforms that
act as the modulation signal for the input.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}-develop

tar xvfz %{SOURCE1}
mv JUCE-6.0.8 juce

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -rav %{__cmake_builddir}/Rotor_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Wed Jul 26 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
