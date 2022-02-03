# Global variables for github repository
%global commit0 c20e56a8eabb2677b0c538d0d056ff48d4cfc971
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Simple Screen Recorder
Name:    ssr
Version: 0.3.8.%{shortcommit0}
Release: 1%{?dist}
License: GPL
URL:     https://github.com/MaartenBaert/ssr

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/MaartenBaert/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: qt4-devel
BuildRequires: ffmpeg-devel
BuildRequires: pulseaudio-libs-devel

%description
SimpleScreenRecorder is a Linux program created to record programs and games. 

%prep
%autosetup -n %{name}-%{commit0}

%build

%configure
%{__make} %{_smp_mflags}

%install

%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

# install polyphon.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Video \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/simplescreenrecorder.desktop

%files
%defattr(-,root,root,-)
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
