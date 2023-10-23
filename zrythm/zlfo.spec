Name:    ZLFO
Version: 0.1.3
Release: 1%{?dist}
Summary: Fully featured LFO for CV-based automation
License: GPL-2.0-or-later
URL:     https://github.com/zrythm/ZLFO

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/zrythm/ZLFO/archive/refs/tags/v0.1.3.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: meson
BuildRequires: ztoolkit

%description
Fully featured LFO for CV-based automation

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s/== 0.1.1/== 0.1.2/g" meson.build

%build

%set_build_flags

export CFLAGS="-fPIC $CFLAGS"

%meson -Dlv2dir=%{_lib}/lv2
%meson_build

%install

%meson_install

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Tue Oct 27 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.3-1
- Initial build
