# Tag: Jack, Delay
# Type: Plugin, LV2
# Category: Audio, Effect

Summary: Pattern-controlled audio stream / sample re-sequencer LV2 plugin
Name:    lv2-BJumblr
Version: 1.6.6
Release: 2%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BJumblr

Source0: https://github.com/sjaehn/BJumblr/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel
BuildRequires: libsndfile-devel

%description
B.Jumblr is neither a sample slicer nor a step sequencer. 
From the technical POV B.Jumblr is a sequencer pattern-controlled audio delay effect.

%prep
%autosetup -n BJumblr-%{version}

%build

%make_build PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -include stdexcept -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -include stdexcept -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Sun Apr 18 2021 Yann Collette <ycollette dot nospam at free.fr> 1.6.6-2
- update to 1.6.6-2

* Mon Mar 15 2021 Yann Collette <ycollette dot nospam at free.fr> 1.6.4-2
- update to 1.6.4-2

* Thu Feb 11 2021 Yann Collette <ycollette dot nospam at free.fr> 1.6.2-2
- update to 1.6.2-2

* Mon Dec 21 2020 Yann Collette <ycollette dot nospam at free.fr> 1.6.0-2
- update to 1.6.0-2

* Wed Nov 4 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.2-2
- update to 1.4.2-2

* Fri Jul 24 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-2
- update to 1.4.0-2

* Thu Jun 25 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.2-2
- update to 1.2.2-2

* Sat May 16 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-2
- update to 1.2.0-2

* Fri Apr 24 2020 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-2
- fix for Fedora 32

* Thu Apr 2 2020 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-1
- initial release 
