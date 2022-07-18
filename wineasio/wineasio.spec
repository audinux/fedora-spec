%global debug_package %{nil}
%define _lto_cflags %{nil}

%global with_32bit  1

%if 0%{?fedora} >= 33
%global wineversion 6.13
%endif
%if 0%{?fedora} >= 34
%global wineversion 7.2
%endif
%if 0%{?fedora} >= 35
%global wineversion 7.2
%endif
%if 0%{?fedora} >= 36
%global wineversion 7.2
%endif

Name: wineasio
Version: 1.1.0
Release: 2%{?dist}
Summary: ASIO to JACK driver for WINE
License: LGPLv2.1
URL: https://github.com/wineasio/wineasio

Source0: https://github.com/wineasio/wineasio/releases/download/v%{version}/wineasio-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: wine-devel >= %{wineversion}
%if %{with_32bit}
BuildRequires: glibc-devel(x86-32)
BuildRequires: jack-audio-connection-kit-devel(x86-32)
BuildRequires: wine-devel(x86-32) >= %{wineversion}
%endif

BuildArch: x86_64

Requires: jack-audio-connection-kit
Requires: wine >= %{wineversion}
# gui
Requires: python3-qt5
%if %{with_32bit}
Requires: jack-audio-connection-kit(x86-32)
Requires: wine(x86-32) >= %{wineversion}
%endif

%description
WineASIO provides an ASIO to JACK driver for WINE. ASIO is the most common
Windows low-latency driver, so is commonly used in audio workstation programs.
You can, for example, use with FLStudio under GNU/Linux systems (together
with JACK).

%prep
%autosetup -p1 -n %{name}-%{version}

%build

%make_build 64

%if %{with_32bit}
%make_build 32
%endif

%install
# create lib dirs
install -d -m0755 %{buildroot}%{_libdir}/wine
%if %{with_32bit}
install -d -m0755 %{buildroot}%{_prefix}/lib/wine
%endif

# install libs
install -D -m 0755 build64/wineasio.dll %{buildroot}%{_libdir}/wine/x86_64-windows/wineasio.dll
install -D -m 0755 build64/wineasio.dll.so %{buildroot}%{_libdir}/wine/x86_64-unix/wineasio.dll.so

%if %{with_32bit}
install -D -m 0755 build32/wineasio.dll %{buildroot}%{_prefix}/lib/wine/i386-windows/wineasio.dll
install -D -m 0755 build32/wineasio.dll.so %{buildroot}%{_prefix}/lib/wine/i386-unix/wineasio.dll.so
%endif

# install gui
pushd gui
%make_install
popd

%files
%license COPYING.LIB COPYING.GUI
%doc README.md

%{_libdir}/wine/x86_64-windows/wineasio.dll
%{_libdir}/wine/x86_64-unix/wineasio.dll.so

%if %{with_32bit}
%{_prefix}/lib/wine/i386-windows/wineasio.dll
%{_prefix}/lib/wine/i386-unix/wineasio.dll.so
%endif

%{_bindir}/wineasio-settings
%dir  %{_datadir}/%{name}
%{_datadir}/%{name}/*.py

%changelog
* Sat Mar 26 2022 Patrick Laimbock <patrick@laimbock.com> - 1.1.0-2
- build against wine-7.5

* Sun Feb 27 2022 Patrick Laimbock <patrick@laimbock.com> - 1.1.0-1
- update to version 1.1.0
- build against wine-7.3

* Sat Jan 01 2022 Patrick Laimbock <patrick@laimbock.com> - 1.1.0-0.3
- build against wine-7.0rc3

* Sun Dec 05 2021 Patrick Laimbock <patrick@laimbock.com> - 1.1.0-0.2
- build against wine-6.23

* Thu Nov 25 2021 Patrick Laimbock <patrick@laimbock.com> - 1.1.0-0.1
- update to version 1.1.0
- build against wine-6.22

* Thu Oct 07 2021 Patrick Laimbock <patrick@laimbock.com> - 1.0.1-0.14
- build against wine-6.18

* Sat Sep 11 2021 Patrick Laimbock <patrick@laimbock.com> - 1.0.1-0.13
- build against wine-6.17

* Sat Aug 28 2021 Patrick Laimbock <patrick@laimbock.com> - 1.0.1-0.12
- build against wine-6.16

* Sat Aug 14 2021 Patrick Laimbock <patrick@laimbock.com> - 1.0.1-0.11
- build against wine-6.15

* Sun Aug 01 2021 Patrick Laimbock <patrick@laimbock.com> - 1.0.1-0.10
- build against wine-6.14

* Thu Jul 22 2021 Patrick Laimbock <patrick@laimbock.com> - 1.0.1-0.9
- build against wine-6.13

* Sun Jun 06 2021 Patrick Laimbock <patrick@laimbock.com> - 1.0.1-0.8
- build against wine-6.10

* Sun May 23 2021 Patrick Laimbock <patrick@laimbock.com> - 1.0.1-0.7
- build against wine-6.9

* Mon May 10 2021 Patrick Laimbock <patrick@laimbock.com> - 1.0.1-0.6
- build against wine-6.8

* Sun Apr 25 2021 Patrick Laimbock <patrick@laimbock.com> - 1.0.1-0.5
- update to git rev 0a97f2f9e29c133349237cdd88fec4615cc72931
- build against wine-6.7

* Sun Apr 11 2021 Patrick Laimbock <patrick@laimbock.com> - 1.0.1-0.4
- build against wine-6.6

* Mon Mar 15 2021 Patrick Laimbock <patrick@laimbock.com> - 1.0.1-0.3
- build against wine 6.4
- fix requires so wineasio does not block a newer wine version

* Sun Feb 28 2021 Patrick Laimbock <patrick@laimbock.com> - 1.0.1-0.2
- build against wine 6.3

* Tue Feb 23 2021 Patrick Laimbock <patrick@laimbock.com> - 1.0.1-0.1
- initial release for Fedora 33

