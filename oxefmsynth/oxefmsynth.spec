# Global variables for github repository
%global commit0 fe078ea036991081c3a28bb388a3fecd0e8e3a5d
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    oxefmsynth
Version: 1.3.5.%{shortcommit0}
Release: 2%{?dist}
Summary: A FM synthetized
License: GPLv2+
URL:     https://github.com/oxesoft/oxefmsynth

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/oxesoft/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: http://ycollette.free.fr/LMMS/vst.tar.bz2
Patch0:  oxefmsynth-fix-cxxflags-override.patch

BuildRequires: gcc gcc-c++
BuildRequires: libX11-devel
BuildRequires: wget
BuildRequires: unzip

%description
A FM Synthesizer

%prep
%autosetup -p1 -n %{name}-%{commit0}

%ifarch aarch64
sed -i -e "s/-m64//g" Makefile.vstlinux
%endif

%build

tar xvfj %{SOURCE1}
export VSTSDK_PATH=vst/vstsdk2.4/

%set_build_flags
export CXXFLAGS="-fPIC $CXXFLAGS"

%make_build 

%install 

export VSTSDK_PATH=vst/vstsdk2.4/

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 oxeconverter %{buildroot}/%{_bindir}/
install -m 755 oxefmsynth %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 *.so %{buildroot}/%{_libdir}/vst/

install -m 755 -d %{buildroot}%{_libdir}/vst/skins/default/
install -m 755 -d %{buildroot}%{_libdir}/vst/skins/dx7/
install -m 755 -d %{buildroot}%{_libdir}/vst/skins/lcd/
install -m 755 -d %{buildroot}%{_libdir}/vst/skins/snow/
install -m 755 -d %{buildroot}%{_libdir}/vst/skins/totolitoto/
install -m 755 -d %{buildroot}%{_libdir}/vst/skins/tx802/

install -m 644 skins/default/*    %{buildroot}/%{_libdir}/vst/skins/default/
install -m 644 skins/dx7/*        %{buildroot}/%{_libdir}/vst/skins/dx7/
install -m 644 skins/lcd/*        %{buildroot}/%{_libdir}/vst/skins/lcd/
install -m 644 skins/snow/*       %{buildroot}/%{_libdir}/vst/skins/snow/
install -m 644 skins/totolitoto/* %{buildroot}/%{_libdir}/vst/skins/totolitoto/
install -m 644 skins/tx802/*      %{buildroot}/%{_libdir}/vst/skins/tx802/

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/*

%changelog
* Wed Oct 21 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.5-2
- fix debug build - fix missing exe

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.3.5-1
- update for Fedora 29
- update to fe078ea036991081c3a28bb388a3fecd0e8e3a5d

* Sun May 13 2018 Yann Collette <ycollette.nospam@free.fr> - 1.3.5-1

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.3.4-1
- Initial build
