# Status: active
# Tag: Tool, Rack
# Type: Standalone
# Category: Audio, Effect, Tool

Name: amplitron
Version: 0.1.180
Release: 2%{?dist}
Summary: Poor man's guitar amp
License: MIT
URL: https://github.com/sudip-mondal-2002/Amplitron
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./amplitron-source.sh <TAG>
#        ./amplitron-source.sh v0.1.180

Source0: Amplitron.tar.gz
Source1: amplitron-source.sh
Patch0: amplitron-0001-fix-nanosvg-header.patch
Patch1: amplitron-0002-remove-some-gcc-options.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: SDL2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: pkgconfig(jack)
BuildRequires: portaudio-devel
BuildRequires: nanosvg-devel
BuildRequires: rtmidi-devel
BuildRequires: desktop-file-utils

%description
Professional real-time guitar amplifier simulator with ultra-low latency,
11 studio-quality effects, and a beautiful visual pedal board interface.
Available as a native desktop app and a browser-based web demo.
Built in C++17 with PortAudio, SDL2, and Dear ImGui.

%prep
%autosetup -p1 -n Amplitron

%build

%cmake
%cmake_build

%install

%cmake_install

# install icon
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
cp assets/icon.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# create desktop file
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=guitar-amp
Icon=%{name}
Comment=Poor man's guitar amp
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md docs/*
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/%{name}/presets/*
%{_datadir}/icons/hicolor/scalable/apps/*

%changelog
* Fri May 15 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.180-2
- update to 0.1.180-2

* Tue May 12 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.171-2
- update to 0.1.171-2

* Mon May 11 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.167-2
- update to 0.1.167-2

* Mon May 11 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.166-2
- update to 0.1.166-2

* Fri Apr 10 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.164-2
- update to 0.1.164-2

* Mon Apr 06 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.138-2
- update to 0.1.138-2

* Thu Apr 02 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.74-2
- update to 0.1.74-2

* Wed Apr 01 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.71-2
- update to 0.1.71-2 - fix preset path

* Tue Mar 31 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.71-1
- Initial spec file
