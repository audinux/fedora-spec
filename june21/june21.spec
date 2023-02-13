Name:    june21
Version: 0.9.6
Release: 1%{?dist}
Summary: Alpha juno 2 emulator using CSound & Cabbage
URL:     https://github.com/mikerodd/june-21
License: GPLv3+

# TODO:
# package cabbage

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/mikerodd/june-21/archive/refs/tags/v0.9.6.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: csound-devel
BuildRequires: alsa-lib-devel
BuildRequires: texlive-pdftex
BuildRequires: texinfo

%description
Roland Juno-1 / Juno-2 / MKS-50 emulator using CSound & Cabbage

%prep
%autosetup -n june-21-%{version}

%build

cd src/plugins/junosyxloader/

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/

# Build documentation

mkdir %{__cmake_builddir}/june-21/

cd src/plugins/junosyxloader/

cp -r ../../doc/manual.pdf %{__cmake_builddir}/june-21/june-21-manual.pdf
cp %{__cmake_builddir}/libjsl.so %{__cmake_builddir}/june-21/

cat ../cabbage-module/june-21.csd | sed  "s/{VERSION}/%{version}/g" > %{__cmake_builddir}/june-21/june-21.csd

cp -R ../../cabbage-module/dat %{__cmake_builddir}/june-21/
cp -R ../../cabbage-module/imgs %{__cmake_builddir}/june-21/
cp -R ../../cabbage-module/presets %{__cmake_builddir}/june-21/
cp -R ../../build/runtime/linux/* %{__cmake_builddir}/june-21/

mv %{__cmake_builddir}/june-21 %{buildroot}%{_libdir}/vst3/

%files
%doc README.md
%license LICENSE
%{_libdir}/vst3/*

%changelog
* Sun Feb 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.6-1
- Initial spec file
