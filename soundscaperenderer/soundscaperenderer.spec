Name:    soundscaperenderer
Version: 0.6.0
Release: 1%{?dist}
Summary: SoundScape Renderer
License: GPLv4+
URL:     https://github.com/SoundScapeRenderer/ssr

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/SoundScapeRenderer/ssr/releases/download/%{version}/ssr-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: qtchooser
BuildRequires: fftw-devel
BuildRequires: libsndfile-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libxml2-devel
BuildRequires: websocketpp-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: fmt-devel
BuildRequires: rapidjson-devel
BuildRequires: asio-devel
BuildRequires: opus-devel

%description
This is the source distribution of SoundScape Renderer (SSR) licensed under the
GPLv3+. Please consult the file COPYING for more information about this license.

The user manual in the doc/ directory contains relevant informations about the
SSR, including installation instructions. Additional (very detailed)
installation instructions can be found in the file INSTALL.

%prep
%autosetup -n ssr-%{version}

%build

export QT_SELECT=5

%configure --disable-ecasound QTMOC=moc-qt5
%make_build

%install

%make_install

install -m 755 -d %{buildroot}/%{_datadir}/ssr/pd/
cp -ra pd/* %{buildroot}/%{_datadir}/ssr/pd/

%files
%doc README
%license COPYING
%{_bindir}/*
%{_datadir}/doc/ssr/*
%{_datadir}/ssr/*
%{_mandir}/*

%changelog
* Wed Feb 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- Initial version
