# Status: active
# Tag: Video, Tool
# Type: Standalone
# Category: Tool

Name: vimix
Version: 0.9.0
Release: 1%{?dist}
Summary: Live Video Mixer
URL: https://github.com/brunoherbelin/vimix
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-or-later

Vendor:       Audinux
Distribution: Audinux

# to get the sources:
# ./vimix-source.sh 0.9.0

Source0: vimix.tar.gz
Source1: vimix-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: patchelf
BuildRequires: mold
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: gstreamer1-plugins-bad-free-devel
BuildRequires: libudev-devel
BuildRequires: libinput-devel
BuildRequires: libicu-devel
BuildRequires: glfw-devel
BuildRequires: glm-devel
BuildRequires: tinyxml2-devel
BuildRequires: stb-devel
BuildRequires: gtk3-devel
BuildRequires: cmrc-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
Vimix performs graphical mixing and blending of several movie clips and computer generated graphics,
with image processing effects in real-time (OpenGL). Vimix supports GPU accelerated decoding and encoding.
Its intuitive and hands-on user interface gives direct control on image opacity and shape for producing
live graphics during concerts and VJ-ing sessions.
Video mapping can be configured for projection on all connected monitors.
The output can also be live streamed (SRT, shared memory) or recorded.

%prep
%autosetup -n %{name}

sed -i -e "/set(CPACK_STRIP_FILES TRUE)/d" CMakeLists.txt
sed -i -e "s/Icon=vimix.svg/Icon=vimix/g" share/applications/vimix.desktop
sed -i -e "s/AudioVideo;Video;Graphics;/AudioVideo;/g" share/applications/vimix.desktop

%build

%cmake -DCMAKE_EXE_LINKER_FLAGS="-fuse-ld=mold"
%cmake_build

%install

%cmake_install
install -m755 %{__cmake_builddir}/src/vimix %{buildroot}/%{_bindir}/

mkdir -p %{buildroot}/%{_libdir}/vimix/

install -m755 %{__cmake_builddir}/libGLAD.so %{buildroot}/%{_libdir}/vimix/
install -m755 %{__cmake_builddir}/libOSCPACK.so %{buildroot}/%{_libdir}/vimix/
install -m755 %{__cmake_builddir}/libIMGUI.so %{buildroot}/%{_libdir}/vimix/
install -m755 %{__cmake_builddir}/libIMGUITEXTEDIT.so %{buildroot}/%{_libdir}/vimix/

patchelf --set-rpath '$ORIGIN/../%{_lib}/vimix/' %{buildroot}/%{_bindir}/vimix

mkdir -p %{buildroot}/%{_datadir}/mime/packages/
mv %{buildroot}/%{_datadir}/applications/io.github.brunoherbelin.Vimix.mime.xml %{buildroot}/%{_datadir}/mime/packages/

# Install desktop file
desktop-file-install                         \
  --add-category="Video"                     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/*.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files
%doc README.md docs/*
%license LICENSE COPYING.txt
%{_bindir}/*
%{_libdir}/vimix/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%{_datadir}/mime/packages/*

%changelog
* Wed Apr 22 2026 Yann Collette <ycollette.nospam@free.fr> - 0.9.0-1
- initial specfile
