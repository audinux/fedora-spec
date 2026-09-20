# Status: active
# Tag: Devel, Tool
# Type: Language
# Category: Tool

%global commit0 ee44de5d857dafab47fc35f34093ebebdf2a7c12

Name: soundscaperenderer
Version: 0.6.1
Release: 2%{?dist}
Summary: SoundScape Renderer
License: GPL-3.0-or-later
URL: https://github.com/SoundScapeRenderer/ssr
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./ssr-source.sh <TAG>
#        ./ssr-source.sh master

Source0: ssr.tar.gz
Source1: ssr-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: qtchooser
BuildRequires: fftw-devel
BuildRequires: libsndfile-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libxml2-devel
BuildRequires: websocketpp-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: fmt-devel
BuildRequires: rapidjson-devel
BuildRequires: asio-devel
BuildRequires: opus-devel
BuildRequires: faad2-devel
BuildRequires: help2man

%description
This is the source distribution of SoundScape Renderer (SSR) licensed under the
GPLv3+. Please consult the file COPYING for more information about this license.

The user manual in the doc/ directory contains relevant informations about the
SSR, including installation instructions. Additional (very detailed)
installation instructions can be found in the file INSTALL.

%prep
%autosetup -n ssr

./autogen.sh

%build

export QT_SELECT=5
export HELP2MAN_LOCALE=C

%configure --disable-ecasound -disable-dynamic-asdf QTMOC=moc-qt5
%make_build

%install

%make_install

install -m 755 -d %{buildroot}/%{_datadir}/ssr/pd/
cp -ra pd/* %{buildroot}/%{_datadir}/ssr/pd/

%files
%doc README
%license COPYING
%{_bindir}/*
%{_datadir}/doc/ssr/
%{_datadir}/ssr/
%{_mandir}/*

%changelog
* Sun Sep 20 2026 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-2
- update to 0.6.1-2 - update to commit ee44de5d857dafab47fc35f34093ebebdf2a7c12

* Sun Sep 20 2026 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-1
- update to 0.6.1-1

* Wed Feb 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- Initial version
