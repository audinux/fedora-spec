# Tag: Editor
# Type: Language
# Category: Audio, Programming

# Global variables for github repository
%global commit0 355f0243480dde6c691e783489793eb445a88967
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    amuc
Version: 1.7.%{shortcommit0}
Release: 3%{?dist}
Summary: Amuc - the Amsterdam Music Composer
License: GPL-2.0-or-later
URL:     https://github.com/pjz/amuc.git

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/pjz/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  amuc-0001-fix-build-with-gcc-7.patch
Patch1:  amuc-0002-add-missing-library.patch
Patch2:  amuc-0003-fix-makefiles.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: cairo-devel
BuildRequires: jack-audio-connection-kit-devel

%description
Amuc - the Amsterdam Music Composer

%prep
%autosetup -p1 -n %{name}-%{commit0}

sed -i -e "s/strip/#strip/g" Makefile

%build

%set_build_flags

%make_build -j1

%install 

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 src/amuc %{buildroot}/%{_bindir}/
install -m 755 src-abcm2ps/abcm2ps %{buildroot}/%{_bindir}/
install -m 755 src-wav2score/wav2score %{buildroot}/%{_bindir}/
install -m 755 src-tr-sco/tr-sco %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/amuc/samples/
install -m 644 samples/* %{buildroot}/%{_datadir}/amuc/samples/
install -m 755 -d %{buildroot}/%{_datadir}/amuc/samples/
install -m 644 samples/* %{buildroot}/%{_datadir}/amuc/samples/
install -m 644 tunes/* %{buildroot}/%{_datadir}/amuc/
install -m 755 -d %{buildroot}/%{_mandir}/man1/
install -m 644 doc/amuc.1 %{buildroot}/%{_mandir}/man1/
install -m 755 -d %{buildroot}/%{_docdir}/amuc/
install -m 644 doc/* %{buildroot}/%{_docdir}/amuc/
rm %{buildroot}/%{_docdir}/amuc/amuc.1

%files
%doc README
%license LICENSE
%{_bindir}/*
%{_datadir}/amuc/
%{_docdir}/amuc/
%{_mandir}/man1/*

%changelog
* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 1.7-3
- fix debug build

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.7-2
- update for Fedora 29

* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 1.7-1
- initial release
