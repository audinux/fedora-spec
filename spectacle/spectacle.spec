Name:    spectacle
Version: 2.0
Release: 1%{?dist}
Summary: Realtime graphical spectrum analyzer
URL:     https://github.com/jpcima/spectacle
License: GPL

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/jpcima/spectacle/releases/download/v2.0/spectacle-analyzer-v%{version}.tar.gz
Source1: spectacle.png

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: lv2-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libglvnd-devel
BuildRequires: fftw-devel
BuildRequires: desktop-file-utils

%description
Spectacle is a real-time spectral analyzer using the short-time Fourier
transform, available as VST / LV2 audio plugin and JACK client.

- display the spectrum on logarithmic musical scale
- control the parameters of the analysis that affect latency and precision
- have zoom functionality and smooth interpolation
- identify the value under cursor and the peaks

%package -n vst-spectacle
Summary: VST Realtime graphical spectrum analyzer

%description -n vst-spectacle
Spectacle is a real-time spectral analyzer using the short-time Fourier
transform.

- display the spectrum on logarithmic musical scale
- control the parameters of the analysis that affect latency and precision
- have zoom functionality and smooth interpolation
- identify the value under cursor and the peaks

%package -n lv2-spectacle
Summary: LV2 Realtime graphical spectrum analyzer

%description -n lv2-spectacle
Spectacle is a real-time spectral analyzer using the short-time Fourier
transform.

- display the spectrum on logarithmic musical scale
- control the parameters of the analysis that affect latency and precision
- have zoom functionality and smooth interpolation
- identify the value under cursor and the peaks

%prep

%autosetup -n spectacle-analyzer-v%{version}

%build

%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" SKIP_STRIPPING=true VERBOSE=true

%install

%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" SKIP_STRIPPING=true VERBOSE=true

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cp %{SOURCE1} %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/spectacle.png

cat > %{buildroot}/%{_datadir}/applications/spectacle-analyzer.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=Spectacle Analyzer
Comment=Realtime graphical spectrum analyzer
Exec=spectacle-analyzer
Icon=spectacle
Terminal=false
Type=Application
Categories=Audio;AudioVideo;
EOF

desktop-file-validate %{buildroot}%{_datadir}/applications/spectacle-analyzer.desktop

desktop-file-install                         \
  --add-category="Audio"                     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/spectacle-analyzer.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/spectacle-analyzer
%{_datadir}/applications/*
%{_datadir}/icons/*

%files -n lv2-spectacle
%{_libdir}/lv2/*
%files -n vst-spectacle
%{_libdir}/vst/*

%changelog
* Thu May 13 2021 Yann Collette <ycollette.nospam@free.fr> - 2.0-1
- Initial spec file
