# Tag: Audio
# Type: Standalone
# Category: Audio, Tool

Name:    fmit
Version: 1.2.14
Release: 1%{?dist}
Summary: Free Music Instrument Tuner
URL:     https://github.com/gillesdegottex/fmit
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/gillesdegottex/fmit/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: itstool
BuildRequires: gettext
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: desktop-file-utils

%description
FMIT is a graphical utility for tuning your musical instruments, with error
and volume history and advanced features like microtonal tuning, statistics,
and various views like waveform shape, harmonics ratios and real-time Discrete
Fourier Transform (DFT). All views and advanced features are optional so that
the interface can also be very simple.

%prep
%autosetup -n %{name}-%{version}

%build

%qmake_qt5 fmit.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 distrib/fmit.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 fmit %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_metainfodir}/
install -m 644 distrib/fmit.appdata.xml %{buildroot}/%{_metainfodir}/

install -m 755 -d %{buildroot}/%{_mandir}/man1/
install -m 755 -d %{buildroot}/%{_mandir}/fr/man1/

install -m 644 distrib/fmit.1 %{buildroot}/%{_mandir}/man1/
install -m 644 distrib/fmit.fr.1 %{buildroot}/%{_mandir}/fr/man1/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 ui/images/fmit.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -m 755 -d %{buildroot}/%{_datadir}/fmit/scales/
cp -ra scales/* %{buildroot}/%{_datadir}/fmit/scales/

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/*.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.txt
%license COPYING_GPL.txt COPYING_LGPL.txt
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/fr/man1/*
%{_metainfodir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/fmit/scales/*

%changelog
* Sat Aug 13 2022 Yann Collette <ycollette.nospam@free.fr> - 1.2.14-1
- Initial spec file
