# Status: active
# Tag: Audio, Modulation, Distortion
# Type: Plugin, LV2
# Category: Audio, Effect

Name: lv2-dkbuilder-guitarix-lv2-plugins
Version: 1.0.1
Release: 1%{?dist}
Summary: LV2 plugins made with dkbuilder 
License: GPL-3.0-or-later
URL: https://github.com/domichel/dkbuilder-guitarix-lv2-plugins
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/domichel/dkbuilder-guitarix-lv2-plugins/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel

%description
dkbuilder is a toolkit that takes gschem electronic schematics as input
and output source code in different formats:
LV2 (native linux audio plugins), guitarix or faust.
The dkbuilder is part of guitarix source code, see
https://linuxmusicians.com/search.php?keywords=dkbuilder for reference on
how to install and use it, and https://github.com/brummer10/guitarix for
its code.

The LV2 plugins can be used with any LV2 capable host (guitarix, jalv, ardour, ...), the faust code will be best used with XUiDesigner: https://github.com/brummer10/XUiDesigner

%prep
%autosetup -n dkbuilder-guitarix-lv2-plugins-%{version}

%build

%set_build_flags

# Force clean
find . -name "*.o" -exec rm {} \;

cd stable/BlowMeAmplifier/buildlv2/
for Files in `ls -d */`
do
    cd $Files
    %make_build STRIP=true INSTALL_DIR=%{_libdir}/lv2
    cd ..
done

%install

cd stable/BlowMeAmplifier/buildlv2/
for Files in `ls -d */`
do
    cd $Files
    %make_install STRIP=true INSTALL_DIR=%{_libdir}/lv2
    cd ..
done

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Sep 30 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- Initial build

