# Tag: Audio, Sequencer
# Type: Plugin, LV2
# Category: Audio, Sequencer

Name: lv2-euclidean-rhythms
Version: 0.1.1
Release: 1%{?dist}
Summary: Implementation of the Euclidean-Rhythms idea in the form of plugin
License: GPL-3.0-only
URL: https://github.com/bruno-unna/euclidean-rhythms
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/bruno-unna/euclidean-rhythms/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: lv2-devel

%description
An implementation of the Euclidean rhythms idea in the form of plugins.

%prep
%autosetup -c -n euclidean-rhythms-%{version}

%ifarch aarch64
sed -i -e "/lib_c_args/d" euclidean-rhythms-%{version}/src/meson.build
%endif

%build

cd euclidean-rhythms-%{version}
%meson
%meson_build

%install

cd euclidean-rhythms-%{version}
%meson_install

%files
%doc euclidean-rhythms-%{version}/README.md
%license euclidean-rhythms-%{version}/LICENCE
%{_libdir}/lv2/*
%exclude %{_libdir}/pkgconfig/
%exclude %{_includedir}/

%changelog
* Sun Feb 19 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.1.1
- Initial development
