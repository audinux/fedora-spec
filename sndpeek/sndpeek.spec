Name:    sndpeek
Version: 1.41
Release: 1%{?dist}
Summary: real-time audio visualization
License: GPL
URL:     https://www.gewang.com/software/sndpeek/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://www.gewang.com/software/sndpeek/files/sndpeek-%{version}.tgz

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
sndpeek is just what it sounds (and looks) like:

- real-time 3D animated display/playback
- can use mic-input or wav/aiff/snd/raw/mat file (with playback)
- time-domain waveform
- FFT magnitude spectrum
- 3D waterfall plot
- lissajous! (interchannel correlation)
- rotatable and scalable display
- freeze frame! (for didactic purposes)
- real-time spectral feature extraction (centroid, rms, flux, rolloff)

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s/-D__LITTLE_ENDIAN__/-D__LITTLE_ENDIAN__ \$(FED_CXXFLAGS)/g" src/sndpeek/makefile.alsa
sed -i -e "s/-D__LITTLE_ENDIAN__/-D__LITTLE_ENDIAN__ \$(FED_CXXFLAGS)/g" src/sndpeek/makefile.jack

%build

%set_build_flags
export FED_CXXFLAGS="$CXXFLAGS"

cd src/sndpeek
%make_build -f makefile.alsa
cp sndpeek sndpeek-alsa
make clean
%make_build -f makefile.jack
cp sndpeek sndpeek-jack

%Install

install -m 755 -d %{buildroot}/%{_bindir}/
cp src/sndpeek/sndpeek-alsa %{buildroot}/%{_bindir}/sndpeek
cp src/sndpeek/sndpeek-jack %{buildroot}/%{_bindir}/sndpeek-jack

%files
%doc README
%license COPYING
%{_bindir}/*

%changelog
* Sun Oct 30 2022 Yann Collette <ycollette.nospam@free.fr> - 1.41-1
- Initial development
