# Tag: Audio, Effect
# Type: Plugin, LV2
# Category: Audio, Effect

Name: lv2-fps-plugins
Version: 1.0beta3
Release: 1%{?dist}
Summary: A collection of plugins
License: GPL-3.0-or-later
URL: https://github.com/fps/fps-plugins.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/fps/fps-plugins.lv2/archive/refs/tags/1beta3.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: libsndfile-devel
BuildRequires: fftw-devel

%description
A collection of plugins

%prep
%autosetup -n fps-plugins.lv2-1beta3

%build

%set_build_flags

%make_build CXX_EXTRA_FLAGS="$CXXFLAGS -I./vendored `pkg-config lv2 sndfile fftw3f --cflags --libs` -fPIC"

%install

%make_install PREFIX=/usr INSTALL_DIR=%{buildroot}/%{_libdir}/lv2

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Fri Jun 09 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0beta3-1
- Initial development
