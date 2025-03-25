# Status: active
# Tag: Plugin, Effect, Audio
# Type: VST3
# Category: Effect, Audio

Name:    maim
Version: 1.1.1
Release: 1%{?dist}
Summary: Audio plugin for custom MP3 distortion and digital glitches
License: GPL-3.0
URL:     https://github.com/ArdenButterfield/Maim
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./maim-source.sh <TAG>
#        ./maim-source.sh v1.1.1

Source0: Maim.tar.gz
Source1: maim-source.sh
Patch0: maim-0001-fix-cmake-file.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: lame-devel
BuildRequires: opus-devel
BuildRequires: webkit2gtk3-devel

%description
MAIM is an audio plugin that circuit bends an MP3 encoder in real time,
disrupting the control flow sending data down unexpected paths to create
digital distortions.
With heavily hacked real MP3 encoders at its core, MAIM gives you the full
gamut of digital distortion, from the realistic to the fantastical.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -p1 -n Maim

%build

cd lib/lame/
%configure CFLAGS="-fPIC" --disable-frontend --enable-expopt=full --disable-shared --enable-static
%make_build
cd ../..

%set_build_flags
export CXXFLAGS="-I/usr/include/opus $CXXFLAGS"
export CFLAGS="-I/usr/include/opus $CFLAGS"

%cmake -DOPUS_X86_PRESUME_SSE4_1:BOOL=OFF \
       -DOPUS_X86_MAY_HAVE_SSE4_1:BOOL=OFF \
       -DOPUS_X86_MAY_HAVE_AVX2:BOOL=OFF \
       -DOPUS_X86_PRESUME_AVX2:BOOL=OFF \
       -DLAME_LIB=lib/lame/./libmp3lame/.libs/libmp3lame.a

%cmake_build

# ERROR   0002: file '/usr/lib64/vst3/Maim.vst3/Contents/x86_64-linux/Maim.so' contains an invalid runpath '/home/ycollette/rpmbuild/BUILD/Maim/redhat-linux-build/opus' in [/home/ycollette/rpmbuild/BUILD/Maim/redhat-linux-build/opus]

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Maim_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_datadir}/%{name}/docs/
cp Docs/Manual.md %{buildroot}%{_datadir}/%{name}/docs/
cp -ra Docs/images %{buildroot}%{_datadir}/%{name}/docs/

%files -n vst3-%{name}
%doc README.md
%license LICENSE
%{_libdir}/vst3/*
%{_datadir}/%{name}/*

%changelog
* Thu Mar 20 2025 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-1
- update to 1.1.1-1

* Wed Dec 06 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
