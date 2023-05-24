# Global variables for github repository
%global commit0 edd5216ac8ad7ef6fc0e6dd02762759db7a15986
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    mod-system-plugins
Version: 0.1.%{shortcommit0}
Release: 1%{?dist}
Summary: LV2 plugin versions of the I/O processing found in the MOD Dwarf
License: GPLv2+
URL:     https://github.com/moddevices/mod-system-plugins

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/moddevices/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel

%description
LV2 plugin versions of the I/O processing found in mod-host.
This includes:
- MOD Compressor
- MOD Compressor Advanced
- MOD Noisegate
- MOD Noisegate Advanced
Note2Midi is EXPERIMENTAL and it's NOT WORKING yet.

%prep
%autosetup -n %{name}-%{commit0}

sed -i -e "s/-Wl,--strip-all//g" Makefile.mk
sed -i -e "s/-Wall/-Wall $\(CFLAGS\)/g" Makefile.mk

for Files in `find . -name Makefile -exec grep -l "/lib/lv2" {} \;`
do
    sed -i -e "s|/lib/lv2|/%{_lib}/lv2|g" $Files
done

%build

%set_build_flags

%make_build PREFIX=/usr

%install

%make_install PREFIX=/usr

# Fix shared libraries permission
find %{buildroot}/%{_libdir}/lv2 -name "*.so" -exec chmod a+rwx {} \;

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Wed May 24 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-edd5216a-1
- Initial build
