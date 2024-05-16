# Tag: Library
# Type: Presets
# Category: Programming

# Global variables for github repository
%global commit0 89abb1b6732a867630b9f2cdb3eef30ec25fda87
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: BatLib
Version: 0.1
Release: 1%{?dist}
Epoch: 1
Summary: Various helper classes I use, and external methods my other Quarks use.
License: Creative Commons Attribution-ShareAlike 4.0 International Public License
URL: https://github.com/supercollider-quarks/%{name}
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/supercollider-quarks/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildArch: noarch

Requires: supercollider

%description
Various helper classes I use, and external methods my other Quarks use.

%prep
%autosetup -n %{name}-%{commit0}

%build

%install

install -m 755 -d %{buildroot}/%{_datadir}/SuperCollider/Quarks/%{name}/
install -m 644 BatLib.quark  CoverMe.sc  Executor.sc   LessKeys.sc  StageLimiter.sc %{buildroot}/%{_datadir}/SuperCollider/Quarks/%{name}/

install -m 755 -d %{buildroot}/%{_datadir}/SuperCollider/Quarks/%{name}/external_methods/
install -m 644 external_methods/score_nrt_notifier.sc external_methods/window_center_rect.sc %{buildroot}/%{_datadir}/SuperCollider/Quarks/%{name}/external_methods/

install -m 755 -d %{buildroot}/%{_datadir}/SuperCollider/Quarks/%{name}/external_methods/osx/scide_scapp/
install -m 644 external_methods/osx/scide_scapp/image_from_sound.sc %{buildroot}/%{_datadir}/SuperCollider/Quarks/%{name}/external_methods/osx/scide_scapp/

%files
%{_datadir}/*

%changelog
* Fri Oct 23 2020 Yann Collette <ycollette dot nospam at free.fr> 0.1.0-1
- initial release of the spec file

* Wed Jun 06 2019 Yann Collette <ycollette dot nospam at free.fr> 0.1.0-1
- initial release of the spec file
