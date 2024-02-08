# Tag: Convolution, Amp Simul
# Type: Plugin, LV2
# Category: Audio, Tool, Plugin

Name: ImpulseLoader
Version: 0.2
Release: 1%{?dist}
Summary: This is a simple, mono, IR-File loader/convolution LV2 plug
License: GPL-2.0-or-later
URL: https://github.com/brummer10/ImpulseLoader.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/brummer10/ImpulseLoader.lv2/releases/download/v%{version}/ImpulseLoader.lv2-v%{version}-src.tar.xz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: git
BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel
BuildRequires: libsndfile-devel
BuildRequires: vim-common

%description
This is a simple, mono, IR-File loader/convolution LV2 plug

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n ImpulseLoader.lv2-v%{version}

%build

%make_build STRIP=true

%install

%make_install INSTALL_DIR=/usr/%{_lib}/lv2 STRIP=true

%files
%doc README.md

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Thu Feb 08 2024 Yann Collette <ycollette.nospam@free.fr> - 0.2-1
- update to 0.2-1

* Wed Feb 07 2024 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial spec file
