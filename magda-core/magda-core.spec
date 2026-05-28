# Status: active
# Tag: Editor, Audio, MIDI, Sequencer
# Type: Standalone
# Category: DAW, MIDI

Name: magda-core
Version: 0.9.1
Release: 2%{?dist}
Summary: A DAW built for automation, transformation, and fast musical iteration
License: GPL-3.0-or-later
URL: https://github.com/Conceptual-Machines/magda-core
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./magda-core-source.sh <TAG>
#        ./magda-core-source.sh v0.9.1

Source0: magda-core.tar.gz
Source1: magda-core-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: git-lfs
BuildRequires: patchelf
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
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk4.1-devel

%description
MAGDA is a free, open-source DAW with AI integrated from the ground up. Built on C++20, JUCE, and Tracktion Engine.
Features:
* Hybrid tracks: every track hosts both audio and MIDI clips
* Three views: Arrangement, Session, and Mix
* AI chat: natural language commands that generate and execute a custom DSL directly in the app (BYOAK, Bring Your Own API Keys)
* Modulation system: 16 LFOs (with bezier curve editor) and 16 macro knobs per device and rack
* Racks: parallel processing chains with volume, pan, mute, solo per chain, fully nestable
* Piano roll with pitchbend and MIDI CC lanes
* Drum grid device
* Session view with clip launching
* Mixer with faders, pan, mute, solo, sends, and I/O routing
* Collapsible, resizable panels: Inspector + AI Chat (left), Plugin Browser + Sample Browser (right), context-sensitive editor (bottom)

%prep
%autosetup -n magda-core

%build

%set_build_flags

%cmake -DMAGDA_BUILD_TESTS=OFF \
       -DMAGDA_BUILD_EXAMPLES=OFF \
       -DCMAKE_CXX_FLAGS="-Wno-template-body `pkg-config --cflags webkit2gtk-4.1` `pkg-config --cflags gtk+-3.0` $CXXFLAGS"
%cmake_build

%install

%cmake_install

# install onnxruntime and fix RPATH
install -m 755 -d %{buildroot}/%{_libdir}/magda-core/
install -m 755 %{__cmake_builddir}/_deps/onnxruntime-src/lib/libonnxruntime.so.1.* %{buildroot}/%{_libdir}/magda-core/
patchelf --set-rpath '$ORIGIN/../%{_lib}/magda-core/' %{buildroot}/%{_bindir}/MAGDA

# cleanup
rm -rf %{buildroot}/%{_bindir}/JUCE*
rm -f %{buildroot}/%{_bindir}/convert_hf_to_gguf.py
rm -rf %{buildroot}/%{_includedir}/
rm -rf %{buildroot}/%{_usr}/lib/cmake
rm -rf %{buildroot}/%{_libdir}/cmake
rm -rf %{buildroot}/%{_libdir}/libggml*.a
rm -rf %{buildroot}/%{_libdir}/libllama.a
rm -rf %{buildroot}/%{_libdir}/pkgconfig

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
mv %{buildroot}/%{_bindir}/controllers %{buildroot}/%{_datadir}/%{name}/
mv %{buildroot}/%{_bindir}/lang %{buildroot}/%{_datadir}/%{name}/

%files
%doc README.md CONTRIBUTING.md SECURITY.md
%license LICENSE
%{_bindir}/*
%{_libdir}/magda-core/*
%{_datadir}/%{name}/controllers/*
%{_datadir}/%{name}/lang/*

%changelog
* Wed May 27 2026 Yann Collette <ycollette.nospam@free.fr> - 0.9.1-2
- update to 0.9.1-2

* Mon May 25 2026 Yann Collette <ycollette.nospam@free.fr> - 0.9.0-2
- update to 0.9.0-2

* Thu May 21 2026 Yann Collette <ycollette.nospam@free.fr> - 0.8.1-2
- update to 0.8.1-2 - fix installation

* Mon May 18 2026 Yann Collette <ycollette.nospam@free.fr> - 0.8.0-1
- update to 0.8.0-1

* Sun May 10 2026 Yann Collette <ycollette.nospam@free.fr> - 0.7.3-1
- update to 0.7.3-1

* Thu May 07 2026 Yann Collette <ycollette.nospam@free.fr> - 0.7.2-1
- update to 0.7.2-1

* Tue May 05 2026 Yann Collette <ycollette.nospam@free.fr> - 0.7.1-1
- update to 0.7.1-1

* Mon May 04 2026 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-1
- update to 0.7.0-1

* Thu Apr 30 2026 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-1
- update to 0.6.1-1

* Tue Apr 28 2026 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-1
- update to 0.6.0-1

* Sat Apr 25 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.7-1
- update to 0.5.7-1

* Sat Apr 25 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.6-1
- update to 0.5.6-1

* Fri Apr 24 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.5-1
- update to 0.5.5-1

* Thu Apr 23 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.4-1
- update to 0.5.4-1

* Wed Apr 22 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.3-1
- update to 0.5.3-1

* Tue Apr 21 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- update to 0.5.2-1

* Mon Apr 20 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- update to 0.5.1-1

* Mon Apr 20 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- update to 0.5.0-1

* Thu Apr 16 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.8-1
- update to 0.4.8-1

* Wed Apr 15 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.7-1
- update to 0.4.7-1

* Tue Apr 14 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.6-1
- update to 0.4.6-1

* Mon Apr 13 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.5-1
- update to 0.4.5-1

* Sun Apr 12 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.4-1
- update to 0.4.4-1

* Sat Apr 11 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.3-1
- update to 0.4.3-1

* Fri Apr 10 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.1-1
- Initial spec file
