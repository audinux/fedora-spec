# Tag: Effect, Synthesizer
# Type: Plugin, LV2
# Category: Effect, Synthesizer

%define commit0 33

Name: lv2-russolo
Version: 0.0.1
Release: 1%{?dist}
Summary: Russolo Suite
License: GPL-3.0-or-later
URL: https://sourceforge.net/projects/intonarumori/

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/code-snapshots/svn/i/in/intonarumori/code/intonarumori-code-r%{commit0}.zip

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel

%description
Standalone, LV2 and VST instruments & effects generating weird sounds,
noises and glitches, for experimental music. Heavily inspired by the
Futurist musician Luigi Russolo, the aim of this project is to create
new instruments for the new century.

%prep
%autosetup -n intonarumori-code-r%{commit0}

sed -i -e "s/lv2core/lv2/g" crazynth/crazynth_stereo/Makefile
sed -i -e "s/lv2core/lv2/g" omnifono/Makefile

sed -i -e "s/-Wall/-Wall \$(RUSSOLO_CFLAGS)/g" crazynth/crazynth_stereo/Makefile
sed -i -e "s/-Wall/-Wall \$(RUSSOLO_CFLAGS)/g" omnifono/Makefile

# File unused heqder
sed -i -e "/include\/eq.h/d" omnifono/omnifx.c

%build

%set_build_flags

export RUSSOLO_CFLAGS="$CFLAGS"

cd crazynth/crazynth_stereo/
%make_build PREFIX=/usr
cd ../..

cd omnifono/
%make_build PREFIX=/usr
cd ..

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra omnifono/Omnifono.lv2 %{buildroot}/%{_libdir}/lv2/
cp -ra crazynth/crazynth_stereo/Crazynth_Stereo.lv2 %{buildroot}/%{_libdir}/lv2/

cp omnifono/README README.omnifono
cp crazynth/crazynth_stereo/README README.crazynth

%files
%doc README.omnifono README.crazynth
%{_libdir}/lv2/*

%changelog
* Sat Jan 21 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial build

