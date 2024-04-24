# Tag: Library, Tool
# Type: Devel, Standalone, Plugin, VST3
# Category: Programming, Effect

Name: vst3sdk
Version: 3.7.11
Release: 1%{?dist}
Summary: VST 3 Plug-In SDK
License: GPL-3.0-or-Later
URL: https://github.com/steinbergmedia/vst3sdk

Vendor: Audinux
Distribution: Audinux

# ./vst3sdk-source.sh <TAG>
# ./vst3sdk-source.sh v3.7.11_build_10

Source0: vst3sdk.tar.gz
Source1: vst3sdk.pc
Source2: vst3sdk-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: rsync
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxcb-devel
BuildRequires: libX11-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: gtkmm30-devel
BuildRequires: sqlite-devel

%description
VST 3 Plug-In SDK

%package -n vst3-%{name}
Summary:  VST3 plugins from %{name}
License:  GPL-3.0-or-later

%description -n vst3-%{name}
VST3 plugins from %{name}

%package src
Summary:  Sources of %{name}
License:  GPL-3.0-or-later

%description src
Sources of %{name}

%package doc
Summary:  Documentation of %{name}
License:  GPL-3.0-or-later

%description doc
Documentation of %{name}

%prep
%autosetup -n %{name}

# Maybe this part is not yet supported on Linux
rm -rf public.sdk/samples/vst/dataexchange/

sed -i -e "s/other.invoke (false);/other.invoke = false;/g" vstgui4/vstgui/lib/finally.h

%build

%cmake -DSMTG_RUN_VST_VALIDATOR=ON
%cmake_build -- VERBOSE=1

%install

%cmake_install

install -m 755 -d %{buildroot}/%{_bindir}/

cp  %{__cmake_builddir}/bin/editorhost %{buildroot}/%{_bindir}/
cp  %{__cmake_builddir}/bin/moduleinfotool %{buildroot}/%{_bindir}/
cp  %{__cmake_builddir}/bin/validator %{buildroot}/%{_bindir}/
cp  %{__cmake_builddir}/bin/Debug/VST3Inspector/VST3Inspector %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -rav %{__cmake_builddir}/VST3/Debug/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_usrsrc}/%{name}/
rsync -r --exclude doc --exclude %{__cmake_builddir} --exclude .git --exclude .github --exclude .gitignore --exclude .gitattributes . %{buildroot}/%{_usrsrc}/%{name}/

install -m 755 -d %{buildroot}/%{_libdir}/cmake/%{name}/
cp -ra cmake/modules/*.cmake %{buildroot}/%{_libdir}/cmake/%{name}/

install -m 755 -d %{buildroot}/%{_libdir}/pkgconfig/
cp %{SOURCE1} %{buildroot}/%{_libdir}/pkgconfig/
sed -i -e "s/VERSION/%{version}/g" %{buildroot}/%{_libdir}/pkgconfig/vst3sdk.pc

install -m 755 -d %{buildroot}/%{_datadir}/doc/%{name}/
cd doc
rsync -r --exclude .git --exclude .github --exclude .gitignore --exclude .gitattributes . %{buildroot}/%{_datadir}/doc/%{name}/

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/*
%files -n vst3-%{name}
%{_libdir}/vst3/*

%files src
%{_usrsrc}/%{name}/*
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/%{name}/*
%{_datadir}/doc/vst3sdk/*

%changelog
* Wed Apr 24 2024 Yann Collette <ycollette.nospam@free.fr> - 3.7.11-1
- update to 3.7.11-1

* Thu Jan 18 2024 Yann Collette <ycollette.nospam@free.fr> - 3.7.10-1
- update to 3.7.10-1

* Sun Jul 23 2023 Yann Collette <ycollette.nospam@free.fr> - 3.7.8-1
- Initial packaging.
