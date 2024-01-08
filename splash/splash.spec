Name:    splash
Version: 0.10.4
Release: 1%{?dist}
Summary: Modular video-mapping software
License: GPL-3.0-only
URL:     https://gitlab.com/splashmapper/splash

Vendor:       Audinux
Distribution: Audinux

# Usage: ./source-splash.sh <tag>
#        ./source-splash.sh 0.10.4

Source0: splash.tar.gz
Source1: source-splash.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: jsoncpp-devel
BuildRequires: gsl-devel
BuildRequires: zeromq-devel
BuildRequires: python3-devel
BuildRequires: opencv-devel
BuildRequires: libgphoto2-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: glm-devel
BuildRequires: libmodplug-devel
BuildRequires: libchromaprint-devel
BuildRequires: portaudio-devel
BuildRequires: ffmpeg-devel
BuildRequires: glfw-devel
BuildRequires: libltc-devel
BuildRequires: doxygen
BuildRequires: snappy-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libuuid-devel
BuildRequires: desktop-file-utils

# cppzmq
# doctest
# flamegraph
# glm
# hap
# imgui
# tracy
# zmq

%description
Splash, a multi-projector video-mapping software

%prep
%autosetup -n %{name}

%build

%set_build_flags

export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`
export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`

%cmake \
    -DBUILD_SHARED_LIBS=ON \
%ifarch x86_64
    -DUSE_SSE2=ON \
    -DUSE_AVX=ON \
%endif
    -DUSE_SYSTEM_LIBS=ON
%cmake_build

%install

%cmake_install

mkdir -p %{buildroot}/%{_datadir}/fonts/%{name}/
mv %{buildroot}/%{_datadir}/fonts/*.ttf %{buildroot}/%{_datadir}/fonts/%{name}/

%files
%license License.md
%doc README.md News.md
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*
%{_datadir}/metainfo/*
%{_datadir}/fonts/%{name}/*
%{_datadir}/%{name}/*

%changelog
* Mon Jan 08 2024 Yann Collette <ycollette.nospam@free.fr> - 0.10.4-1
- update to 0.10.4-1

* Tue Dec 05 2023 Yann Collette <ycollette.nospam@free.fr> - 0.10.2-1
- update to 0.10.2-1

* Mon Nov 13 2023 Yann Collette <ycollette.nospam@free.fr> - 0.10.0-1
- update to 0.10.0-1

* Mon Oct 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.40-1
- Initial spec file
