Summary: Reboot of Non Mixer with eXTended LV2 support.
Name:    non-mixer-xt
Version: 1.1.0
Release: 1%{?dist}
License: GPL-3.0-only
URL:     https://github.com/Stazed/non-mixer-xt

Vendor:       Audinux
Distribution: Audinux

# Usage: ./source-non-mixer-xt.sh <tag>
#        ./source-non-mixer-xt.sh 1.1.0

Source0: non-mixer-xt.tar.gz
Source1: source-non-mixer-xt.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: non-ntk-devel
BuildRequires: non-ntk-fluid
BuildRequires: liblo-devel
BuildRequires: libsndfile-devel
BuildRequires: fltk-fluid
BuildRequires: fltk-devel
BuildRequires: libsigc++20-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libXpm-devel
BuildRequires: ladspa-devel
BuildRequires: liblrdf-devel
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: suil-devel
BuildRequires: zix-devel
BuildRequires: clap-devel
BuildRequires: desktop-file-utils

%description
Non-Mixer-XT is a reboot of original Non-Mixer with eXTended LV2 support.
LV2 support includes X11, ShowInterface and External custom UI support.
In addition, MIDI support with JACK timebase support and much more.
The generic parameter editor has been redesigned to accommodate larger
LV2 plugins, preset support and state save and restore.

%prep
%autosetup -n %{name}

%build

%cmake
%cmake_build

%install
%cmake_install

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=X-Jack \
        --dir %{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/*.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*
%{_datadir}/doc/non-mixer-xt/*

%changelog
* Fri Dec 08 2023 Yann Collette <ycollette dot nospam at free.fr> 1.1.0-1
- update to 1.1.0-1

* Tue Oct 31 2023 Yann Collette <ycollette dot nospam at free.fr> 1.0.6-1
- update to 1.0.6-1

* Thu Oct 26 2023 Yann Collette <ycollette dot nospam at free.fr> 1.0.5-1
- update to 1.0.5-1

* Sat Sep 09 2023 Yann Collette <ycollette dot nospam at free.fr> 1.0.4-1
- initial release
