# Tag: Editor, Analyzer
# Type: Standalone
# Category: Graphic, Tool, Audio

Name: marsyas
Version: 0.5.0
Release: 1%{?dist}
Summary: Marsyas - Music Analysis, Retrieval and Synthesis for Audio Signals
License: GPL-2.0-or-later
URL: https://github.com/marsyas/marsyas

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/marsyas/marsyas/archive/refs/tags/version-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: chrpath

%description
MARSYAS is a software framework for rapid prototyping of audio applications,
with flexibility and extensibility as primary concerns.

It was created by George Tzanetakis as part of his research at Princeton
University as a Phd graduate student, beginning in his first year of graduate
school (1998) when he rewrote various tools that he had been using in order to
make his life easier and also to code them the way he wanted them to be. It
started as a collection of classes written in C++ and JAVA for various sound
analysis and synthesis tasks.

It has grown into a large collection of C++ sound processing modules and a
flexible, intuitive and easy-to-use system to interconnect them. It provides
bindings for Python and integration into other frameworks like PureData,
Max/MSP, openFrameworks, Qt... It also contains a number of applications built
using the framework to facilitate and demonstrate various sound processing
tasks.

MARSYAS is maintained and developed by George Tzanetakis and other
researchers and guided mostly by their own research goals. Anyone who finds
in it anything useful is welcome to use it, but we have no responsibility
whatsoever. Aside from new development, we will try to maintain existing
functionality, and we will be happy to answer any questions and provide help
whenever possible.

MARSYAS is released as free software under the GNU public licence hoping that
it will attract people to contribute to its development. Please see the file
COPYING for licensing details.

For documentation, we recommend reading the online version:
http://marsyas.info/

To report issues and provide suggestions, please use our GitHub project page:
https://github.com/marsyas/marsyas

%package devel
Summary: Headers for developing programs that will use %{name}
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the headers that programmers will
need to develop applications which will use %{name}.

%prep
%autosetup -n %{name}-version-%{version}

sed -i -e "1i #include <QPainterPath>" src/otherlibs/qwt/qwt_painter.cpp
sed -i -e "1i #include <QPainterPath>" src/otherlibs/qwt/qwt_painter_command.cpp
sed -i -e "1i #include <QPainterPath>" src/otherlibs/qwt/qwt_painter_command.h
sed -i -e "1i #include <QPainterPath>" src/otherlibs/qwt/qwt_null_paintdevice.cpp
sed -i -e "1i #include <QPainterPath>" src/otherlibs/qwt/qwt_widget_overlay.cpp
sed -i -e "1i #include <QPainterPath>" src/otherlibs/qwt/qwt_plot_renderer.cpp
sed -i -e "1i #include <QPainterPath>" src/otherlibs/qwt/qwt_plot_panner.cpp

%build

%cmake
%cmake_build

%install

%cmake_install

for Files in %{buildroot}/%{_bindir}/*
do
  chrpath --delete $Files
done
mv %{buildroot}/usr/lib %{buildroot}/%{_libdir}
chrpath --delete $Files %{buildroot}/%{_libdir}/*.so

%files
%doc README
%license COPYING

%{_bindir}/*
%{_libdir}/*.so
%exclude %{_libdir}/*.a

%files devel
%{_includedir}/marsyas/*

%changelog
* Thu Aug 11 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- Initial build
