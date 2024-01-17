Name:    valentine
Version: 0.0.5
Release: 1%{?dist}
Summary: An open source compressor meant to pump and breathe
License: GPL-3.0-or-later
URL:     https://github.com/tote-bag-labs/valentine

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./source-valentine.sh v0.0.5

Source0: valentine.tar.gz
Source1: source-valentine.sh

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
# BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel

%description
Valentine is a compressor and distortion processor. It was inspired
by the hyper compressed and crushed textures in the seminal Justice
record, †. Using it is easy: turning input up makes the signal louder,
more compressed, and more saturated.
Turning crush up adds digital distortion.

The real fun is in processing signal with some ambience, be it a room
or a reverb. With the right input gain and release settings,
you can introduce pumping and breathing artifacts.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}

%build

%set_build_flags

%cmake -DCMAKE_CXX_FLAGS="$CXXFLAGS -include cstdint"
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_bindir}

cp -ra %{__cmake_builddir}/Valentine_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Valentine_artefacts/Standalone/* %{buildroot}%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Thu Apr 27 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.5-1
- update to 0.0.5-1

* Tue Apr 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.4-1
- Initial spec file
