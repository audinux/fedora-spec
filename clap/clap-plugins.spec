# Status: inactive
# Tag: Effect
# Type: Plugin, CLAP
# Category: Audio, Effect

%define commit0 f21ad7f23e12692afc4d97188b1055c6ca515720
%define _lto_cflags %{nil}

Summary: Example clap plugins
Name: clap-plugins
Version: 1.0.1
Release: 3%{?dist}
License: MIT
URL: https://github.com/free-audio/clap-plugins
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./clap-source.sh <project> <tag>
# ./clap-source.sh clap-plugins 38b379ce918160d2d8e7dc6fa06b283000bae980

Source0: clap-plugins.tar.gz
Source1: clap-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtdeclarative-devel

%description
Example Clap Plugins

%prep
%autosetup -n %{name}

%build

%set_build_flags
export CXXFLAGS="-fPIC $CXXFLAGS"
export CFLAGS="-fPIC $CFLAGS"

%cmake
%cmake_build -- -j1

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_libndir}/clap/*

%changelog
* Thu Dec 11 2025 Yann Collette <ycollette dot nospam at free.fr> 1.0.1-3
- update to f21ad7f23e12692afc4d97188b1055c6ca515720

* Tue Mar 11 2025 Yann Collette <ycollette dot nospam at free.fr> 1.0.1-2
- update to 38b379ce918160d2d8e7dc6fa06b283000bae980

* Mon Jan 22 2024 Yann Collette <ycollette dot nospam at free.fr> 1.0.1-1
- initial release
