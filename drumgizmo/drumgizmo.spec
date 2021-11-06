# Tag: Jack, Alsa, Drum
# Type: Plugin, Standalone, LV2
# Category: Audio, Sampler

Summary: Software Synthesizer
Name:    drumgizmo
Version: 0.9.19
Release: 2%{?dist}
License: GPL
URL:     https://www.drumgizmo.org/wiki/doku.php

Vendor:       Audinux
Distribution: Audinux

Source0: https://www.drumgizmo.org/releases/drumgizmo-%version/drumgizmo-%version.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: chrpath
BuildRequires: gettext

# Drumgizmo LV2 plugin
BuildRequires: lv2-devel
BuildRequires: zita-resampler-devel
BuildRequires: libsndfile-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel

# Drumgizmo command-line tools
BuildRequires: expat-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsmf-devel
BuildRequires: alsa-lib-devel

%description
Open source, multichannel, multilayered, cross-platform drum plugin and stand-alone application.
It enables you to compose drums in midi and mix them with a multichannel approach.
It is comparable to that of mixing a real drumkit that has been recorded with a multimic setup.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

export CXXFLAGS="-std=c++11 -include cstdint $CXXFLAGS"

%configure --enable-lv2 --libdir=%{_libdir} 
# --disable-cli --with-lv2dir=

%make_build

%install

%make_install

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/drumgizmo

%files
%doc AUTHORS ChangeLog INSTALL NEWS README
%license COPYING
%{_bindir}/*
%{_libdir}/*
%{_datadir}/man/*

%changelog
* Sun Nov 22 2020 Yann Collette <ycollette dot nospam at free.fr> 0.9.19-2
- update to 0.9.19-2

* Thu Oct 24 2019 Yann Collette <ycollette dot nospam at free.fr> 0.9.18.1-2
- update to 0.9.18.1-2

* Tue Oct 15 2019 Yann Collette <ycollette dot nospam at free.fr> 0.9.18-2
- update to 0.9.18-2

* Thu Jul 18 2019 Yann Collette <ycollette dot nospam at free.fr> 0.9.17-2
- update to 0.9.17-2

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 0.9.16-2
- update for Fedora 29

* Sun Aug 12 2018 Yann Collette <ycollette dot nospam at free.fr> 0.9.16-2

* Sat May 12 2018 Yann Collette <ycollette dot nospam at free.fr> 0.9.15-2

* Sat May 12 2018 Yann Collette <ycollette dot nospam at free.fr> 0.9.14-2

* Mon Oct 23 2017 Yann Collette <ycollette dot nospam at free.fr> 0.9.14-1

* Thu May 12 2016 Yann Collette <ycollette dot nospam at free.fr> 0.9.10-1

* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 0.9.8.1-1
- Initial release of spec fil to 0.9.8.1
