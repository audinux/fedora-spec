# Tag: Guitar, Amp Simul
# Type: Plugin, LV2
# Category: Audio, Effect

Name: xuidesigner
Version: 1.0
Release: 1%{?dist}
Summary: X11 LV2 GUI design tool for libxputty
License: GPL-2.0-or-later
URL: https://github.com/brummer10/XUiDesigner

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./brummer10-source.sh XUiDesigner 7ad91a5102ff8dee2f82dde452b103014b33dbc9

Source0: XUiDesigner.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc
BuildRequires: make
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: lilv-devel
BuildRequires: vim-common
BuildRequires: desktop-file-utils

%description
X11 LV2 GUI design tool for libxputty

%prep
%autosetup -n XUiDesigner

sed -i -e "s|#! /usr/bin/python|#! /usr/bin/python3|g" tools/dsp2cc

# Don't strip
sed -i -e "s| -s | |g" Makefile
sed -i -e "s| -s | |g" XUiDesigner/Makefile

%build

%set_build_flags
export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`
export LDFLAGS=`echo $LDFLAGS | sed -e "s/-Werror=format-security//g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`

%make_build STRIP=true

%install

%make_install INSTALL_DIR=%{_libdir} STRIP=true

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 -p XUiDesigner.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 -p XUiDesigner/XUiDesigner.desktop %{buildroot}%{_datadir}/applications/

desktop-file-install --vendor '' \
        --dir %{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/XUiDesigner.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/XUiDesigner.desktop

%files
%doc README.md
%{_bindir}/*
%{_includedir}/*
%{_datadir}/*
%{_libdir}/*

%changelog
* Thu Jan 04 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- update to 1.0-1

* Sat Nov 19 2022 Yann Collette <ycollette.nospam@free.fr> - 0.9-1
- update to 0.9-1

* Wed Oct 05 2022 Yann Collette <ycollette.nospam@free.fr> - 0.8-1
- update to 0.8-1

* Mon Sep 12 2022 Yann Collette <ycollette.nospam@free.fr> - 0.7-1
- update to 0.7-1

* Sun Sep 04 2022 Yann Collette <ycollette.nospam@free.fr> - 0.6-1
- update to 0.6-1

* Mon Aug 08 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5-1
- update to 0.5-1

* Thu Jul 07 2022 Yann Collette <ycollette.nospam@free.fr> - 0.4-1
- update to 0.4-1

* Sun Nov 14 2021 Yann Collette <ycollette.nospam@free.fr> - 0.3-1
- update to 0.3-1

* Fri Oct 15 2021 Yann Collette <ycollette.nospam@free.fr> - 0.2-1
- Initial spec file
