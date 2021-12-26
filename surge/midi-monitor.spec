Name:    midi-monitor
Version: 30072020
Release: 1%{?dist}
Summary: A JUCE-based midi monitor
License: GPLv2+

# To get the sources, use:
# $ ./source-midi-monitor.sh main

URL:     https://github.com/surge-synthesizer/midi-monitor
Source0: midi-monitor.tar.gz
Source1: source-midi-monitor.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: rsync
BuildRequires: git
BuildRequires: python3
BuildRequires: alsa-lib-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: pkgconfig(webkit2gtk-4.0)

%description
A JUCE-based midi monitor

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}

%build

%cmake
%cmake_build

%install 

export HOME=`pwd`
mkdir .vst3

install -m 755 -d %{buildroot}%{_bindir}/
cp -r %{__cmake_builddir}/midi-monitor_artefacts/Standalone/* %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_libdir}/vst3/MidiMonitor.vst3/
cp -r %{__cmake_builddir}/midi-monitor_artefacts/VST3/MidiMonitor.vst3/* %{buildroot}/%{_libdir}/vst3/MidiMonitor.vst3/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sun Dec 26 2021 Yann Collette <ycollette.nospam@free.fr> - 30072020-1
- Initial spec file
