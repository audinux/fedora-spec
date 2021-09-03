# Tag: Jack, Sequencer
# Type: Plugin, LV2
# Category: Audio, Effect

Summary: Audio glitch effect sequencer LV2 plugin
Name:    lv2-BOops
Version: 1.8.2
Release: 2%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BOops

Source0: https://github.com/sjaehn/BOops/archive/%{version}.tar.gz#/BOops-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: libsndfile-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
Key features:
- Multi-effect plugin controlled by step sequencer patterns
- Apply glitch effects in live or on a sample track
- 30 effects
- Up to 12 effect slots, freely select effects and effect order
- Random effects: 3 different ways of randomization
- Autoplay, host controlled, or MIDI controlled playback
- Up to 16 patterns, MIDI controlled pattern change

%prep
%autosetup -n BOops-%{version}

%build

%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Fri Sep 03 2021 Yann Collette <ycollette dot nospam at free.fr> 1.8.2-2
- update to 1.8.2-2 

* Mon Aug 30 2021 Yann Collette <ycollette dot nospam at free.fr> 1.8.0-2
- update to 1.8.0-2 

* Sat Jun 26 2021 Yann Collette <ycollette dot nospam at free.fr> 1.6.4-2
- update to 1.6.4-2fix spec 

* Sat Jun 26 2021 Yann Collette <ycollette dot nospam at free.fr> 1.6.2-2
- fix spec 

* Sat Jun 12 2021 Yann Collette <ycollette dot nospam at free.fr> 1.6.2-1
- update to 1.6.2-1 

* Fri Jun 04 2021 Yann Collette <ycollette dot nospam at free.fr> 1.6.0-1
- update to 1.6.0-1 

* Fri May 21 2021 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-1
- update to 1.4.0-1 

* Sat May 08 2021 Yann Collette <ycollette dot nospam at free.fr> 1.2.10-1
- update to 1.2.10-1 

* Mon Mar 15 2021 Yann Collette <ycollette dot nospam at free.fr> 1.2.8-1
- update to 1.2.8-1 

* Thu Feb 11 2021 Yann Collette <ycollette dot nospam at free.fr> 1.2.6-1
- update to 1.2.6-1 

* Mon Jan 18 2021 Yann Collette <ycollette dot nospam at free.fr> 1.2.4-1
- update to 1.2.4-1 

* Sun Dec 27 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.2-1
- update to 1.2.2-1 

* Sat Dec 5 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-1
- update to 1.2.0-1 

* Sat Nov 07 2020 Yann Collette <ycollette dot nospam at free.fr> 0.1-1
- initial release 
