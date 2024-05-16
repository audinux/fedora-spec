# Tag: Tool, Audio
# Type: Standalone
# Category: Audio, Tool

Name: lv2file
Version: 0.95
Release: 1%{?dist}
Summary: A simple program which you can use to apply effects to your audio files.
License: GPL-3.0-or-later
URL: https://github.com/jeremysalwen/lv2file
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/jeremysalwen/lv2file/archive/refs/tags/upstream/0.95.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: argtable-devel
BuildRequires: libsndfile-devel

%description
lv2file is a simple program which you can use to apply effects
to your audio files without much hassle. Possible use cases are:
  * When you want to apply an effect without having to open a
  GUI or start a project.
  * When you want to apply effects to a large number of files,
  or in an automated manner.
  * When you need a deterministic environment to debug a plugin.
  * You like everything to be on the command line.
lv2file uses the LV2 plugin format (http://lv2plug.in/) for
the effects it uses.

%prep
%autosetup -n %{name}-upstream-%{version}

%build

%set_build_flags
%make_build

%install

%make_install

install -m 755 -d %{buildroot}/%{_datadir}/man/man1
install -m 644 lv2file.1 %{buildroot}/%{_datadir}/man/man1/

%files
%doc README
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Aug 09 2022 Yann Collette <ycollette.nospam@free.fr> - 0.95-1
- Initial development
