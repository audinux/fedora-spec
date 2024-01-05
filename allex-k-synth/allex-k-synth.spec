# Tag: Synthesizer
# Type: Standalone
# Category: Audio, Synthesizer

Name:    allex-k-synth
Version: 0.0.1
Release: 1%{?dist}
Summary: A synthesizer implemented using JUCE framework. Combines additive, subtractive, wavetable, operator(frequency modulation) synthesis methods
License: GPL-3.0-or-later
URL:     https://github.com/allex-k/synth

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/allex-k/synth/archive/refs/heads/main.zip#/%{name}-master.zip
Source1: Builds.tar.gz
Source2: allex-k-synth.png

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: JUCE60
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
BuildRequires: desktop-file-utils

%description
A synthesizer implemented using JUCE framework. Combines additive,
subtractive, wavetable, operator(frequency modulation) synthesis methods

%prep
%autosetup -n synth-main

tar xvfz %{SOURCE1}

%build

cd Builds/LinuxMakefile/
%make_build

%install

cd Builds/LinuxMakefile/

 install -m 755 -d %{buildroot}/%{_bindir}/
cp  build/synth %{buildroot}/%{_bindir}/allex-k-synth

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Exec=%{name}
Icon=%{name}
Comment=Allex K Synth
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
%doc README.md
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Thu Jul 27 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
