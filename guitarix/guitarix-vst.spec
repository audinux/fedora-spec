# Tag: Guitar, Emulator, Overdrive, Amp Simul, Cabinet, Effect
# Type: Plugin, VST3
# Category: Audio, Effect

Name: vst3-guitarix
Version: 0.3
Release: 1%{?dist}
Summary: guitarix vst3 wrapper
License: GPL-2.0-or-later
URL: https://github.com/brummer10/guitarix.vst
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./brummer10-source.sh guitarix.vst v0.3

Source0: guitarix.vst.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: git
BuildRequires: gtk3-devel
BuildRequires: glib2-devel
BuildRequires: avahi-gobject-devel
BuildRequires: avahi-glib-devel
BuildRequires: freetype-devel
BuildRequires: lilv-devel
BuildRequires: eigen3-devel
BuildRequires: libsndfile-devel
BuildRequires: fftw-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: glibmm2.4-devel
BuildRequires: boost-devel
BuildRequires: vim-common

Requires: guitarix

%description
This is a VST3 wrapper for Guitarix

%prep
%autosetup -n guitarix.vst

sed -i -e "/JUCE_CXXFLAGS += -march=x86/d" Builds/LinuxMakefile/Makefile

%build

%make_build STRIP=true CONFIG=Release

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra Builds/LinuxMakefile/build/Guitarix.vst3 %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md
%{_libdir}/vst3/*

%changelog
* Mon Mar 11 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3-1
- update to 0.3-1

* Fri Feb 23 2024 Yann Collette <ycollette.nospam@free.fr> - 0.2-1
- update to 0.2-1

* Mon Feb 12 2024 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
