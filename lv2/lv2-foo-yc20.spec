# Tag: Audio, Organ
# Type: Plugin, LV2
# Category: Synthesizer

Name: lv2-foo-yc20-plugins
Version: 1.3.0
Release: 1%{?dist}
Summary: This is a Faust implementation of a 1969 designed Yamaha combo organ
License: LGPL2.1
URL: https://github.com/sampov2/foo-yc20

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/sampov2/foo-yc20/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildReauires: make
BuildRequires: lv2-devel
BuildRequires: gtk2-devel
BuildRequires: cairo-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libsndfile-devel
BuildRequires: glib2-devel
BuildRequires: desktop-file-utils

%description
This is a Faust implementation of a 1969 designed Yamaha combo organ, the YC-20.

%prep
%autosetup -n foo-yc20-%{version}

%build
%set_build_flags
%make_build PREFIX=/usr

%install
%make_install PREFIX=/usr

%ifarch amd64 x86_64 aarch64
install -m 755 -d %{buildroot}%{_libdir}/
mv %{buildroot}/usr/lib/lv2 %{buildroot}/%{_libdir}/lv2
%endif

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/foo-yc20.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/foo-yc20.desktop

%files
%doc README
%license LICENSE
%{_bindir}/*
%{_libdir}/lv2/*
%{_datadir}/applications/*
%{_datadir}/foo-yc20/
%{_datadir}/foo-yc20/graphics/*

%changelog
* Wed Dec 07 2022 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-1
- Initial build

