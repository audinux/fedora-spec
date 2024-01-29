# Tag: Synthesizer, Jack
# Type: Standalone, VST3, LV2, Plugin
# Category: Audio, Synthesizer

Name: grainbow
Version: 1.0.2
Release: 1%{?dist}
Summary: A synthesizer that uses pitch detection to choose candidates for granular synthesis or sampling
License: GPL-3.0-or-later
URL: https://github.com/bboettcher3/gRainbow

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-grainbow.sh v1.0.2

Source0: gRainbow.tar.gz
Source1: source-grainbow.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: alsa-lib-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: pkgconfig(jack)
BuildRequires: desktop-file-utils

%description
A synthesizer that uses pitch detection to choose candidates for granular synthesis or sampling.
gRainbow was created to overcome a few shortcomings of traditional granular synths.
- Pitch variations in the input clip can produce inharmonic tones, which isn't always wanted.
  This leads users to often use short single-pitch clips, restricting the synth to a single timbre.
- Manual pitch matching to the input clip is often required to produce the correct notes with MIDI
  input, which can be difficult and repetitive.
- Pitch shifting is commonly done with timestretching, which can create unwanted artifacts when
  shifting multiple octaves in either direction.

Instead, gRainbow prefers longer, pitch-diverse audio clips (1), automatically produces harmonics
matched for MIDI input (2) and avoids too much timestretching by generating harmonics that are
already near their target pitch (3). Voila!

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n gRainbow

%build

%set_build_flags

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/

cp %{__cmake_builddir}/gRainbow_artefacts/Standalone/gRainbow %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/gRainbow_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/gRainbow_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_datadir}/icons/
cp Source/Resources/logo.png %{buildroot}/%{_datadir}/icons/gbow.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/grainbow.desktop <<EOF
[Desktop Entry]
Categories=AudioVideo;Audio;
Comment=Granular synthesizer
Exec=gRainbow
GenericName=gRainbow
Icon=gbow
MimeType=
Name=gRainbow
NoDisplay=false
Path=
StartupNotify=true
Terminal=false
TerminalOptions=
Type=Application
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/grainbow.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/grainbow.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Mon Jan 29 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-1
- update to 1.0.2-1

* Tue Jan 23 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- update to 1.0.1-1

* Thu Oct 26 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.1-1
- update to 0.4.1-1

* Sat Jul 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- Initial spec file
