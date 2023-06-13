Name:    ZLFO
Version: 0.1.3
Release: 1%{?dist}
Summary: Fully featured LFO for CV-based automation
License: GPL-2.0-or-later
URL:     https://git.zrythm.org/cgit/ZLFO/

Vendor:       Audinux
Distribution: Audinux

Source0: https://git.zrythm.org/cgit/ZLFO/snapshot/ZLFO-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: meson
BuildRequires: ztoolkit

%description
Fully featured LFO for CV-based automation

%prep
%autosetup -n %{name}-%{version}

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
