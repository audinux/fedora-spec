# Tag: Tool
# Type: Standalone
# Category: Tool

%global commit0 efb54c043ca2791dfb571e54263df4954491509c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%define debug_package %{nil}

Name:    dxsyx
Version: 0.0.1.%{shortcommit0}
Release: 1%{?dist}
Summary: A C++ library for manipulating DX7 SysEx files.
License: GPLv3+
URL:     https://github.com/rogerallen/dxsyx
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/rogerallen/dxsyx/archive/%{commit0}.zip#/%{name}-%{commit0}.zip

BuildRequires: gcc-c++ make
BuildRequires: lv2-devel
BuildRequires: lvtk

Requires: dxsyx

%description
I created this after using the Dexed VST in Reaper.
See https://github.com/asb2m10/dexed I wanted an easier way to create
my own syx files after finding it difficult to keep track of the
voices I found in the .syx files I found. One good source
is http://homepages.abdn.ac.uk/mth192/pages/html/dx7.html

Plus, I was looking for a C++ project to check out C++11 coding.

%prep
%autosetup -n dxsyx-%{commit0}

%build

%set_build_flags
%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc/

install -m 755 bin/dxsyx %{buildroot}/%{_bindir}/
install -m 755 doc/* %{buildroot}/%{_datadir}/%{name}/doc/

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/*
%{_datadir}/%{name}/doc/*

%changelog
* Tue Jun 13 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1.efb54c04-1
- Initial build

