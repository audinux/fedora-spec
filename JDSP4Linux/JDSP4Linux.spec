Name: jamesdsp
Version: 2.3
Release: 1%{?dist}
Summary: An audio effect processor for PipeWire clients
License: GPLv3
URL: https://github.com/theAeon/JDSP4Linux/

# ./JDSP4Linux-source.sh <tag>
# ./JDSP4Linux-source.sh jamesdsp-2.3-1

Source0: JDSP4Linux.tar.gz
Source1: JDSP4Linux-source.sh

BuildRequires: libarchive-devel
BuildRequires: (qt5-qtbase-devel >= 5.12.8 or libqt5-qtbase-devel >= 5.12.8)
BuildRequires: (qt5-qtbase-private-devel or libqt5-qtbase-private-headers-devel)
BuildRequires: (qt5-qtsvg-devel >= 5.12.8 or libqt5-qtsvg-devel >= 5.12.8)
BuildRequires: gcc-c++
BuildRequires: glibmm24-devel
BuildRequires: glib2-devel
BuildRequires: pipewire-devel
BuildRequires: make

Requires: pipewire >= 0.3

%description
James DSP for Linux

%prep
%autosetup -n JDSP4Linux

%build

%qmake_qt5 JDSP4Linux.pro
%make_build

%install

install -D -m 755 src/jamesdsp %{buildroot}/%{_bindir}/jamesdsp
install -D -m 644 resources/icons/icon.png %{buildroot}/%{_datadir}/pixmaps/jamesdsp.png
install -D -m 644 resources/icons/icon.svg %{buildroot}/%{_datadir}/hicolor/scalable/apps/jamesdsp.svg
install -D -m 755 meta/jamesdsp.desktop %{buildroot}/%{_datadir}/applications/jamesdsp.desktop

%files
%license LICENSE
%{_bindir}/jamesdsp
%{_datadir}/pixmaps/jamesdsp.png
%{_datadir}/hicolor/scalable/apps/jamesdsp.svg
%{_datadir}/applications/jamesdsp.desktop

%changelog
* Fri Dec 31 2021 Andrew Robbins <andrew@robbinsa.me> 2.3-1
- initial version of the spec
