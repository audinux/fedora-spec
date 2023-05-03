Summary:ALSA Scarlett Gen 2/3 Control Panel
Name: alsa-scarlett-gui
Version: 0.2
Release: 1%{?dist}
License: GPLv2+
URL: https://github.com/geoffreybennett/alsa-scarlett-gui

Vendor:       Audinux
Distribution: Audinux

Source: https://github.com/geoffreybennett/alsa-scarlett-gui/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: gtk4-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils

%description 
The Focusrite Scarlett interfaces are class compliant USB audio interfaces meaning
that they work “out of the box” on Linux as audio and MIDI interfaces (although on
Gen 3 you need to disable MSD mode first).
However, the Gen 2 6i6+ and Gen 3 4i4+ interfaces have a bunch of proprietary
functionality that required a kernel driver to be written specifically for those
devices.

%prep
%autosetup 

sed -i -e "s/-Wall -Werror/-Wall \$(CFLAGS)/g" src/Makefile
sed -i -e "/Value=1.5/d" src/vu.b4.alsa-scarlett-gui.desktop.template

%build

%set_build_flags

export CFLAGS=`echo $CFLAGS | sed -e "s|-Werror=format-security||g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s|-Werror=format-security||g"`
export LDFLAGS=`echo $LDFLAGS | sed -e "s|-Werror=format-security||g"`

cd src
%make_build PREFIX=/usr

%install

%set_build_flags

export CFLAGS=`echo $CFLAGS | sed -e "s|-Werror=format-security||g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s|-Werror=format-security||g"`
export LDFLAGS=`echo $LDFLAGS | sed -e "s|-Werror=format-security||g"`

cd src
%make_install PREFIX=/usr
cd ..

DOCDIR=%{buildroot}/%{_datadir}/%{name}/doc/
mkdir -p $DOCDIR/img
mkdir $DOCDIR/demo
cp *.md $DOCDIR/
cp img/* $DOCDIR/img
cp demo/* $DOCDIR/demo

mv %{buildroot}/%{_datadir}/applications/vu.b4.alsa-scarlett-gui.desktop %{buildroot}/%{_datadir}/applications/alsa-scarlett-gui.desktop

desktop-file-install                         \
  --add-category="Audio;AudioVideo"          \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md USAGE.md INTERFACES.md
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/%{name}/doc/*
%{_datadir}/applications/alsa-scarlett-gui.desktop
%{_datadir}/icons/hicolor/256x256/apps/alsa-scarlett-gui.png

%changelog
* Mon Jul 04 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2-1
- initial build
