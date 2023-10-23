Name:    DIE-Plugins
Version: 1.1
Release: 1%{?dist}
Summary: DISTRHO Imported Effect Plugins
License: GPL-2.0-or-later
URL:     https://github.com/DISTRHO/DIE-Plugins

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/DISTRHO/DIE-Plugins/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: lv2-devel
BuildRequires: libsndfile-devel
BuildRequires: glib2-devel

%description
This is a collection of plugins imported into the DISTRHO project for easy packaging.
They are simply to die for ;)

DIE stands for DISTRHO Imported Effect.
It is a play on words from the first imported plugins, "ACE", from the Ardour project.

Imported plugins have their bundle and URIs renamed, in order to make them compatible with the originals.

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s/-Wl,--strip-all//g" Makefile.base.mk

%build

%set_build_flags

%make_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra bin/* %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Mar 15 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1-1
- Initial build
