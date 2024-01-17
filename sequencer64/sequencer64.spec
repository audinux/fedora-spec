Name:    sequencer64
Version: 0.97.1
Release: 4%{?dist}
Summary: MIDI sequencer
License: GPL
URL:     https://github.com/ahlstromcj/sequencer64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ahlstromcj/sequencer64/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: https://github.com/ahlstromcj/sequencer64-doc/archive/0.95.2.tar.gz#/%{name}-doc-0.95.2.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: git
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: gtkmm24-devel
BuildRequires: rtmidi-devel
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

%description
Sequencer64 is a reboot of seq24, extending it with many new features.
The heart of seq24 remains intact.

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%package doc
Summary:  Documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description doc
The %{name}-doc package contains documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}

tar xvfz %{SOURCE1}

%build

%set_build_flags

sh autogen.sh

%if 0%{?fedora} >= 38
CXXFLAGS="-std=c++11 -include cstdint $CXXFLAGS" %configure --enable-rtmidi
%else
%configure --enable-rtmidi
%endif
%make_build CXXFLAGS="$CXXFLAGS"

%install

%make_install

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc/
install -m 644 %{name}-doc-0.95.2/pdf/sequencer64-user-manual.pdf %{buildroot}%{_datadir}/%{name}/doc/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
cp debian/sequencer64.desktop %{buildroot}/%{_datadir}/applications/

install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp desktop/seq64.xpm %{buildroot}/%{_datadir}/pixmaps/sequencer64.xpm

install -m 755 -d %{buildroot}%{_metainfodir}
cp desktop/metainfo/seq64.appdata.xml %{buildroot}%{_metainfodir}/sequencer64.appdata.xml

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/sequencer64.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/sequencer64.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.appdata.xml

%files
%doc ChangeLog INSTALL NEWS README.md README.jack VERSION TODO
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*
%exclude %{_datadir}/%{name}/doc/**

%files devel
%{_includedir}/*

%files doc
%{_datadir}/%{name}/doc/**

%changelog
* Sun Feb 19 2023 Yann Collette <ycollette.nospam@free.fr> - 0.97.1-4
- update to 0.97.1-4 - add metainfo

* Sun Feb 19 2023 Yann Collette <ycollette.nospam@free.fr> - 0.97.1-3
- update to 0.97.1-3

* Fri May 14 2021 Yann Collette <ycollette.nospam@free.fr> - 0.97.0-3
- update to 0.97.0

* Tue Oct 20 2020 Yann Collette <ycollette.nospam@free.fr> - 0.96.8-3
- fix debug build

* Mon Jul 6 2020 Yann Collette <ycollette.nospam@free.fr> - 0.96.8-2
- update to 0.96.8-2

* Tue May 5 2020 Yann Collette <ycollette.nospam@free.fr> - 0.96.7-2
- update to 0.96.7-2 - add documentation

* Tue May 5 2020 Yann Collette <ycollette.nospam@free.fr> - 0.96.7-1
- update to 0.96.7-1

* Mon Nov 19 2018 L.L.Robinson <baggypants@fedoraproject.org> - 0.96.1-1
- initial version
