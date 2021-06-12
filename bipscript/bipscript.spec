# Tag: Jack, Alsa
# Type: Standalone, Language
# Category: Audio, Programming

Name:    bipscript
Version: 0.12
Release: 1%{?dist}
Summary: Audio language
URL:     https://www.bipscript.org/
License: GPLv2+

# original tarfile can be found here:
Source0: https://gitlab.domainepublic.net/bipscript/bipscript/-/archive/v%{version}/bipscript-v%{version}.tar.gz
Source1: bipscrip-example.bip

BuildRequires: gcc gcc-c++
BuildRequires: lilv-devel
BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: liblo-devel
BuildRequires: portsmf-devel
BuildRequires: libsndfile-devel
BuildRequires: boost-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: cmake

%description
Bipscript is a scripting language for creating music.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build

%cmake

%cmake_build

%install

%cmake_install

install -m 755 -d %{buildroot}/%{_datadir}/bipscript/example/
install -m 755 %{SOURCE1} %{buildroot}/%{_datadir}/bipscript/example/example.bip

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%changelog
* Sat Apr 17 2021 Yann Collette <ycollette.nospam@free.fr> - 0.12-1
- Initial build
