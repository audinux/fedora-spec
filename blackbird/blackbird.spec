# Tag: Jack, Synthesizer
# Type: Standalone, VST3
# Category: Audio, Synthesizer

Name:    blackbird
Version: 0.1.0
Release: 1%{?dist}
Summary: VST3 Synth built with JUCE
License: GPL-3.0-or-later
URL:     https://github.com/khrykin/BlackBird
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/khrykin/BlackBird/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: Build.tar.gz
Source2: blackbird.png

BuildRequires: gcc gcc-c++
BuildRequires: cmake
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
BuildRequires: JUCE60
BuildRequires: vst3sdk
BuildRequires: desktop-file-utils

%description
VST3 Synth built with JUCE

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n BlackBird-%{version}

tar xvfz %{SOURCE1}

%build

cd Builds/LinuxMakefile/
%make_build CONFIG=Release

%install

cd Builds/LinuxMakefile/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -rav build/BlackBird.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_bindir}/
cp build/BlackBird %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/blackbird/presets/
cp ../../Resources/Presets/* %{buildroot}/%{_datadir}/blackbird/presets/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%name
Exec=BlackBird
Icon=blackbird
Comment=BlackBird Synth
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
# Result: 45 tests passed, 2 tests failed
# validator %{buildroot}/%{_libdir}/vst3/BlackBird.vst3

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/*
%{_datadir}/blackbird/presets/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Tue Jul 25 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial spec file
