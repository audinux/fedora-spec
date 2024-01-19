# Tag: Analyzer, Effect
# Type: Standalone
# Category: Effect

Name: rt_pvc
Version: 1.0.0
Release: 1%{?dist}
Summary: real-time phase vocoder analysis/synthesis library + visualization
License: GPL
URL: https://soundlab.cs.princeton.edu/software/rt_pvc/

Vendor:       Audinux
Distribution: Audinux

Source0: https://soundlab.cs.princeton.edu/software/rt_pvc/rt_pvc-%{version}.tgz
Patch0: rt_pvc-0001-fix-build.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: libsndfile-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: freeglut-devel
BuildRequires: libXmu-devel
BuildRequires: libXext-devel
BuildRequires: libXi-devel

%description
rt_pvc is a:
- real-time phase vocoder library for synthesis/analysis
- vocoder application that allows the user to do time-expansion, frequency expansion, and cross-synthesis in real-time, from mic-input or from file.
- real-time phase vocoder visualization
- learning tool that teaches about the phase vocoder and its implemementation
- open source!

%prep
%autosetup -p1 -c -n %{name}-%{version}

%build

%set_build_flags

export FED_CFLAGS="$CFLAGS"
export FED_CXXFLAGS="-std=c++11 -include cstdio -include cstring $CXXFLAGS"

%make_build -f makefile.alsa
cp rt_pvc rt_pvc-alsa
make -f makefile.alsa clean
%make_build -f makefile.jack
cp rt_pvc rt_pvc-jack

%Install

install -m 755 -d %{buildroot}/%{_bindir}/
cp rt_pvc-alsa %{buildroot}/%{_bindir}/rt_pvc
cp rt_pvc-jack %{buildroot}/%{_bindir}/rt_pvc-jack

%files
%{_bindir}/*

%changelog
* Sun Oct 30 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial development
