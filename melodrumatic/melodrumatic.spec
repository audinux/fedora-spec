Name:    melodrumatic
Version: 0.1.3
Release: 1%{?dist}
Summary: Audio plugin that lets you use MIDI to pitch-shift via delay to turn unpitched audio into melodies
License: GPL-3.0-or-later
URL:     https://github.com/usdivad/Melodrumatic

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/usdivad/Melodrumatic/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: Melodrumatic.jucer

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: JUCE60
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
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel

%description
Melodrumatic is an audio plugin that lets you "pitch-shift" via delay
(i.e. the Doppler effect) to turn unpitched audio into melodies.
Controllable via MIDI or mouse.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n Melodrumatic-%{version}

cp %{SOURCE1} .

%build

%set_build_flags

Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Melodrumatic.jucer

cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true

%install 

install -m 755 -d %{buildroot}%{_bindir}/
cp Builds/LinuxMakefile/build/Melodrumatic %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra Builds/LinuxMakefile/build/Melodrumatic.vst3 %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Mon Jan 30 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.3-1
- Initial spec file
