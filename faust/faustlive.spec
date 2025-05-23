# Status: active
# Tag: Editor
# Type: Standalone, Language
# Category: Tool

Name: faustlive
Version: 2.5.19
Release: 1%{?dist}
Summary: The swiss knife for Faust development
License: GPL-2.0-or-later
URL: https://github.com/grame-cncm/faustlive
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# to get source:
# ./faustlive-source.sh 2.5.19

Source0: faustlive.tar.gz
Source1: faustlive-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: libsndfile-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: faust
BuildRequires: faust-devel
BuildRequires: faust-osclib-devel
BuildRequires: alsa-lib-devel
BuildRequires: libcurl-devel
%if 0%{?fedora} <= 39
BuildRequires: llvm-devel
%elif 0%{?fedora} == 40
BuildRequires: llvm16-devel
%else
BuildRequires: llvm17-devel
%endif
BuildRequires: desktop-file-utils

Requires: faust

%description
FaustLive is an advanced self-contained prototyping environment for
the Faust programming language with an ultra-short edit-compile-run
cycle.
Thanks to its fully embedded compilation chain, FaustLive is simple
to install and doesn't require any external compiler, development
toolchain or SDK to run.

FaustLive is the ideal tool for fast prototyping. Faust programs can
be compiled and run on the fly by simple drag and drop.
They can even be edited and recompiled while running, without sound
interruption. It supports also native applications generation using
the Faust online compiler.

FaustLive is based on the Faust library and on LLVM.

%prep
%autosetup -n %{name}

sed -i -e "1 i #include <list>" src/Audio/JA/JA_audioFader.h
sed -i -e "2 i using std::list;" src/Audio/JA/JA_audioFader.h

%build

%if 0%{?fedora} == 40
export PATH=$PATH:/usr/lib64/llvm16/bin
%elif 0%{?fedora} >= 41
export PATH=$PATH:/usr/lib64/llvm17/bin
%endif

%set_build_flags
export LDFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"

cd Build
%cmake
%cmake_build

%install

cd Build
%cmake_install

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/FaustLive.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/FaustLive.desktop

%files
%doc README.md
%license GPL.txt
%{_bindir}/*
%{_datadir}/applications/FaustLive.desktop
%{_datadir}/doc/faustlive/UserManual.pdf
%{_datadir}/doc/faustlive/faust-quick-reference.pdf
%{_datadir}/icons/hicolor/32x32/apps/FaustLiveIcon.png
%{_datadir}/icons/hicolor/scalable/apps/Faustlive.svg
%{_datadir}/pixmaps/Faustlive.xpm

%changelog
* Sat Sep 21 2024 Yann Collette <ycollette.nospam@free.fr> - 2.5.19-1
- update to 2.5.19-1

* Tue Apr 02 2024 Yann Collette <ycollette.nospam@free.fr> - 2.5.18-1
- update to 2.5.18-1

* Sat Jan 06 2024 Yann Collette <ycollette.nospam@free.fr> - 2.5.17-1
- update to 2.5.17-1

* Sat Oct 07 2023 Yann Collette <ycollette.nospam@free.fr> - 2.5.15-1
- initial spec file
