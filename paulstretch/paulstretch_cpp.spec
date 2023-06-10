%global commit0 7f5c3993abe420661ea0b808304b0e2b4b0048c5

Name:    paulstretch_cpp
Version: 2.1.0
Release: 1%{?dist}
Summary: The Paulstretch program
License: GPL-2.0-only
URL:     https://github.com/paulnasca/paulstretch_cpp

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/paulnasca/paulstretch_cpp/archive/%{commit0}.zip#/%{name}-%{version}.zip
# Icon downloaded from: https://www.flaticon.com/free-icons/audio
Source1: paulstretch_cpp_audio-waves.png
Patch0: https://github.com/paulnasca/paulstretch_cpp/pull/12.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: mxml-devel
BuildRequires: audiofile-devel
BuildRequires: libvorbis-devel
BuildRequires: fltk-devel
BuildRequires: fltk-fluid
BuildRequires: portaudio-devel
BuildRequires: libmad-devel
BuildRequires: fftw-devel
BuildRequires: libsamplerate-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: desktop-file-utils

%description
The original PaulStretch program

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build

./compile_linux_fftw_jack.sh
cp paulstretch paulstretch-jack

./compile_linux_fftw.sh

%install 

install -m 755 -d %{buildroot}%{_bindir}/

cp paulstretch %{buildroot}%{_bindir}/
cp paulstretch-jack %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/icons/%{name}/
install -m 644 -p %{SOURCE1} %{buildroot}/%{_datadir}/icons/%{name}/audio-wave.png

install -m 755 -d %{buildroot}%{_datadir}/applications/

cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=PaulStretch_Cpp Alsa
Comment=Audio stretcher
Exec=paulstretch
Icon=/usr/share/icons/paulstretch_cpp/audio-wave.png
Terminal=false
Type=Application
Categories=Audio;AudioVideo;
EOF

cat > %{buildroot}/%{_datadir}/applications/%{name}-jack.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=PaulStretch_Cpp Jack
Comment=Audio stretcher
Exec=paulstretch-jack
Icon=/usr/share/icons/paulstretch_cpp/audio-wave.png
Terminal=false
Type=Application
Categories=Audio;AudioVideo;
EOF

desktop-file-install                         \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

desktop-file-install                         \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-jack.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-jack.desktop

%files
%doc readme.txt
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/%{name}/

%changelog
* Tue Jan 17 2023 Yann Collette <ycollette.nospam@free.fr> - 2.1.0-1
- Initial spec file
