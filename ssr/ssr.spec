# Tag: Video, Tool, Jack
# Type: Standalone
# Category: Tool

Summary: Simple Screen Recorder
Name: ssr
Version: 0.4.4
Release: 1%{?dist}
License: GPL
URL: https://github.com/MaartenBaert/ssr

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/MaartenBaert/ssr/archive/refs/tags/0.4.4.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: qt4-devel
BuildRequires: ffmpeg-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: desktop-file-utils

%description
SimpleScreenRecorder is a Linux program created to record programs and games.

%prep
%autosetup -n %{name}-%{commit0}

%build

%configure
%make_build

%install

%make_install

# install polyphon.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Video \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/simplescreenrecorder.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/simplescreenrecorder.desktop

%files
%doc AUTHORS.md CHANGELOG.md README.md
%license COPYING
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 0.3.6-1
- update for Fedora 29

* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 0.3.6-1
- Initial release of spec fil to 0.3.6
