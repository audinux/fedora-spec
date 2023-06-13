# Global variables for github repository
%global commit0 0dd7c8149a6cedf9904fddad259ee4d12998d030
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    mod-neural-amp
Version: 0.1.%{shortcommit0}
Release: 1%{?dist}
Summary: An LV2 plugin based on aidadsp-lv2 that directly contains model files within the plugin.
License: GPL-2.0-or-later
URL:     https://github.com/moddevices/mod-neural-amp

Vendor:       Audinux
Distribution: Audinux

# ./moddevices-source.sh <PROJECT> <commit0>
# ./moddevices-source.sh mod-neural-amp 0dd7c8149a6cedf9904fddad259ee4d12998d030

Source0: mod-neural-amp.tar.gz
Source1: moddevices-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel

%description
An LV2 plugin based on aidadsp-lv2 that directly contains model files within the plugin.
It is not a loader, instead it provides a parameter list for the active model.

%prep
%autosetup -n %{name}

sed -i -e "/target_include_directories/a \${CMAKE_BINARY_DIR}" CMakeLists.txt
sed -i -e "s/lib\/lv2/%{_lib}\/lv2/g" CMakeLists.txt

%build

%set_build_flags
export LDFLAGS="$LDFLAGS -z muldefs"

%cmake
%cmake_build

%install

%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Tue May 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-0dd7c814-1
- Initial build
