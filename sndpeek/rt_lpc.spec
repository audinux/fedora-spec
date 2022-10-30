Name:    rt_lpc
Version: 1.0
Release: 1%{?dist}
Summary: real-time LPC analysis + synthesis + visualization
License: GPL
URL:     https://soundlab.cs.princeton.edu/software/rt_lpc/

Vendor:       Audinux
Distribution: Audinux

Source0: https://soundlab.cs.princeton.edu/software/rt_lpc/files/rt_lpc-%{version}.tgz
Patch0: rt_lpc-0001-fix-build.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: libsndfile-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: freeglut-devel
BuildRequires: libXmu-devel
BuildRequires: libXext-devel
BuildRequires: libXi-devel

%description
rt_lpc is a light-weight application that performs real-time
LPC analysis and synthesis. It features the following:

- real-time LPC analysis
- real-time LPC synthesis
- visualization of original, predicted, and error waveforms
- visualization of vocal tract shape from LPC coefficients
- adjustable LPC analysis order
- adjustable synthesis pitch shift
- MIDI controlled pitch (hit 'm')
- lots of other choices (pitch pulse source selection, emphasis filter)
- STFT plot
- modular LPC library 

%prep
%autosetup -p1 -n %{name}-%{version}

%build

%set_build_flags
export FED_CFLAGS="$CFLAGS"
export FED_CXXFLAGS="-include cstring $CXXFLAGS"

cd src
%make_build -f makefile.alsa
cp rt_lpc rt_lpc-alsa
make clean
%make_build -f makefile.jack
cp rt_lpc rt_lpc-jack

%Install

install -m 755 -d %{buildroot}/%{_bindir}/
cp src/rt_lpc-alsa %{buildroot}/%{_bindir}/rt_lpc
cp src/rt_lpc-jack %{buildroot}/%{_bindir}/rt_lpc-jack

%files
%doc README
%license COPYING
%{_bindir}/*

%changelog
* Sun Oct 30 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial development
