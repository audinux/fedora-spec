# Tag: Guitar, Amp Simul
# Type: Plugin, LV2
# Category: Audio, Effect

%global debug_package %{nil}

Name:    xuidesigner
Version: 0.4
Release: 1%{?dist}
Summary: X11 LV2 GUI design tool for libxputty
License: GPLv2+
URL:     https://github.com/brummer10/XUiDesigner

Vendor:       Audinux
Distribution: Audinux

# To get the source archive: ./xuidesigner-source.sh <tag>
# ./xuidesigner-source.sh v0.4

Source0: XUiDesigner.tar.gz
Source1: xuidesigner-source.sh

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

%build

%set_build_flags
export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`
export LDFLAGS=`echo $LDFLAGS | sed -e "s/-Werror=format-security//g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`
export CFLAGS="-fPIC $CFLAGS"
export CXXFLAGS="-fPIC $CXXFLAGS"
export LDFLAGS="-fPIC $LDFLAGS"

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
* Thu Jul 97 2022 Yann Collette <ycollette.nospam@free.fr> - 0.4-1
- update to 0.4-1

* Sun Nov 14 2021 Yann Collette <ycollette.nospam@free.fr> - 0.3-1
- update to 0.3-1

* Fri 15 Oct 2021 Yann Collette <ycollette.nospam@free.fr> - 0.2-1
- Initial spec file
