# Tag: Live, MIDI, Editor
# Type: IDE, Language
# Category: Audio, Programming

Name:    common-music
Version: 3.10.2
Release: 3%{?dist}
Summary: Common Music (CM) is a real-time music composition system implemented in JUCE/C++ and Scheme.
URL:     https://sourceforge.net/projects/commonmusic
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

# original tarfile can be found here:
Source0: https://sourceforge.net/projects/commonmusic/files/cm/%{version}/cm-%{version}.zip

BuildRequires: gcc gcc-c++ make
BuildRequires: premake4
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: gsl-devel
BuildRequires: freetype-devel
BuildRequires: gtk3-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libXext-devel
BuildRequires: libXinerama-devel

%description
Common Music is a music composition system that transforms high-level algorithmic representations of musical processes and structure into a variety of control protocols for sound synthesis and display.
Its main user application is Grace (Graphical Realtime Algorithmic Composition Environment) a drag-and-drop, cross-platform app implemented in JUCE (C++) and S7 Scheme.
In Grace musical algorithms can run in real time, or faster-than-real time when doing file-based composition.
Grace provides two coding languages for designing musical algorithms: S7 Scheme, and SAL, an easy-to-learn but expressive algol-like language.

%prep
%autosetup -n cm-%{version}

# For Fedora 29
%if 0%{?fedora} >= 29
  sed -i -e "112,123d" juce/modules/juce_graphics/colour/juce_PixelFormats.h
%endif

%build

find juce/modules -type f -exec chmod a-x {} \;

%set_build_flags

premake4 --with-jack
# Remove strip option for debug symbol generation
sed -i -e "s/-L. -s/-L./g" Grace.make
%make_build config=release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 bin/Grace %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/cm/res/
cp -ra res/* %{buildroot}/%{_datadir}/cm/res/

%files
%doc readme.text
%{_bindir}/*
%{_datadir}/cm/
%{_datadir}/cm/res/*

%changelog
* Thu Oct 22 2020 Yann Collette <ycollette.nospam@free.fr> - 3.10.2-3
- fix debug build

* Thu May 2 2019 Yann Collette <ycollette.nospam@free.fr> - 3.10.2-2
- Fix release mode and fix for Fedora 30

* Mon Mar 4 2019 Yann Collette <ycollette.nospam@free.fr> - 3.10.2-1
- initial specfile
