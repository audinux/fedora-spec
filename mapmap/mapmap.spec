# Status: active
# Tag: Editor, Video
# Type: Standalone
# Category: Graphic, Tool

%global commit0 cc29e940385aa85c14a28832b20315dc2378b89d

Name: mapmap
Version: 0.6.2
Release: 2%{?dist}
Summary: Open source video mapping software
URL: https://mapmapteam.github.io
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/mapmapteam/mapmap/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-gui
BuildRequires: qt6-qtsvg-devel
BuildRequires: qt6-qtmultimedia-devel
BuildRequires: qt6-linguist
BuildRequires: alsa-lib-devel
BuildRequires: zlib-devel
BuildRequires: glib2-devel
BuildRequires: liblo-devel
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: libsndfile-devel
BuildRequires: desktop-file-utils

%description
MapMap is a free video mapping software.

Projection mapping, also known as video mapping and spatial augmented reality,
is a projection technology used to turn objects, often irregularly shaped,
into a display surface for video projection. These objects may be complex
industrial landscapes, such as buildings. By using specialized software,
a two or three dimensional object is spatially mapped on the virtual program
which mimics the real environment it is to be projected on. The software can
interact with a projector to fit any desired image onto the surface of
that object.
This technique is used by artists and advertisers alike who can add extra
dimensions, optical illusions, and notions of movement onto previously static
objects. The video is commonly combined with, or triggered by,
audio to create an audio-visual narrative.

%prep
%autosetup -n %{name}-%{commit0}

%build

%qmake_qt6 mapmap.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 resources/texts/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 %{name} %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 resources/images/logo/%{name}.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
install -m 644 resources/texts/%{name}.xml %{buildroot}/%{_datadir}/mime/packages/

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc OSC README.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%changelog
* Sun Oct 04 2026 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-2
- update to 0.6.2-2

* Sat Nov 07 2020 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-1
- Initial spec file
