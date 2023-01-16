# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Effect

%define commit0 5360f1b47ec123db4f1cc046745e313bdd44e4d0

Name:    audio-effects
Version: 1.0.0
Release: 1%{?dist}
Summary: A collection of VST3 Synthesizer
License: GPLv2+
URL:     https://github.com/TheWaveWarden/odin2

Vendor:       Audinux
Distribution: Audinux

# Usage: ./audio-effects-sources.sh <TAG>
# ./audio-effects-sources.sh master

# Icon from https://www.flaticon.com/free-icons/sound-effect
Source0: Audio-Effects.tar.gz
Source1: jucer.tar.gz
Source2: audio-effects.png
Source3: audio-effects-source.sh

BuildRequires: gcc gcc-c++ make
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: JUCE60
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: desktop-file-utils

%description
Collection of audio effects plugins implemented from the explanations in
the book "Audio Effects: Theory, Implementation and Application"
by Joshua D. Reiss and Andrew P. McPherson. 

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n Audio-Effects

tar xvfz %{SOURCE1}

%build

%set_build_flags

cd Chorus
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Chorus.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Compressor-Expander
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Compressor-Expander.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Delay
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Delay.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Distortion
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Distortion.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Flanger
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Flanger.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Panning
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Panning.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Parametric\ EQ
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Parametric\ EQ.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Phaser
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Phaser.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Ping-Pong\ Delay
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Ping-Pong\ Delay.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Pitch\ Shift
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Pitch\ Shift.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Ring\ Modulation
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Ring\ Modulation.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Robotization-Whisperization
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Robotization-Whisperization.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Template\ Frequency\ Domain
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Template\ Frequency\ Domain.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Template\ Time\ Domain
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Template\ Time\ Domain.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Tremolo
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Tremolo.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Vibrato
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Vibrato.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Wah-Wah 
Projucer60 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE60/modules/
Projucer60 --resave Wah-Wah.jucer
cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true
cd ../../..

%install 

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_bindir}/

install -m 755 -p Chorus/Builds/LinuxMakefile/build/Chorus %{buildroot}/%{_bindir}/
cp -ra Chorus/Builds/LinuxMakefile/build/Chorus.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Compressor-Expander/Builds/LinuxMakefile/build/Compressor-Expander %{buildroot}/%{_bindir}/
cp -ra Compressor-Expander/Builds/LinuxMakefile/build/Compressor-Expander.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Delay/Builds/LinuxMakefile/build/Delay %{buildroot}/%{_bindir}/
cp -ra Delay/Builds/LinuxMakefile/build/Delay.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Distortion/Builds/LinuxMakefile/build/Distortion %{buildroot}/%{_bindir}/
cp -ra Distortion/Builds/LinuxMakefile/build/Distortion.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Flanger/Builds/LinuxMakefile/build/Flanger %{buildroot}/%{_bindir}/
cp -ra Flanger/Builds/LinuxMakefile/build/Flanger.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Panning/Builds/LinuxMakefile/build/Panning %{buildroot}/%{_bindir}/
cp -ra Panning/Builds/LinuxMakefile/build/Panning.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Parametric\ EQ/Builds/LinuxMakefile/build/Parametric\ EQ %{buildroot}/%{_bindir}/
cp -ra Parametric\ EQ/Builds/LinuxMakefile/build/Parametric\ EQ.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Phaser/Builds/LinuxMakefile/build/Phaser %{buildroot}/%{_bindir}/
cp -ra Phaser/Builds/LinuxMakefile/build/Phaser.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Ping-Pong\ Delay/Builds/LinuxMakefile/build/Ping-Pong\ Delay %{buildroot}/%{_bindir}/
cp -ra Ping-Pong\ Delay/Builds/LinuxMakefile/build/Ping-Pong\ Delay.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Pitch\ Shift/Builds/LinuxMakefile/build/Pitch\ Shift %{buildroot}/%{_bindir}/
cp -ra Pitch\ Shift/Builds/LinuxMakefile/build/Pitch\ Shift.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Ring\ Modulation/Builds/LinuxMakefile/build/Ring\ Modulation %{buildroot}/%{_bindir}/
cp -ra Ring\ Modulation/Builds/LinuxMakefile/build/Ring\ Modulation.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Robotization-Whisperization/Builds/LinuxMakefile/build/Robotization-Whisperization %{buildroot}/%{_bindir}/
cp -ra Robotization-Whisperization/Builds/LinuxMakefile/build/Robotization-Whisperization.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Template\ Frequency\ Domain/Builds/LinuxMakefile/build/Template\ Frequency\ Domain %{buildroot}/%{_bindir}/
cp -ra Template\ Frequency\ Domain/Builds/LinuxMakefile/build/Template\ Frequency\ Domain.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Template\ Time\ Domain/Builds/LinuxMakefile/build/Template\ Time\ Domain %{buildroot}/%{_bindir}/
cp -ra Template\ Time\ Domain/Builds/LinuxMakefile/build/Template\ Time\ Domain.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Tremolo/Builds/LinuxMakefile/build/Tremolo %{buildroot}/%{_bindir}/
cp -ra Tremolo/Builds/LinuxMakefile/build/Tremolo.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Vibrato/Builds/LinuxMakefile/build/Vibrato %{buildroot}/%{_bindir}/
cp -ra Vibrato/Builds/LinuxMakefile/build/Vibrato.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -p Wah-Wah/Builds/LinuxMakefile/build/Wah-Wah %{buildroot}/%{_bindir}/
cp -ra Wah-Wah/Builds/LinuxMakefile/build/Wah-Wah.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps/audio-effects.png

#
# Desktop files
#

install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/Chorus.desktop <<EOF
[Desktop Entry]
Name=Chorus
Exec=Chorus
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Chorus
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Compressor-Expander.desktop <<EOF
[Desktop Entry]
Name=Compressor-Expander
Exec=Compressor-Expander
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Compressor-Expander
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Delay.desktop <<EOF
[Desktop Entry]
Name=Delay
Exec=Delay
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Delay
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Distortion.desktop <<EOF
[Desktop Entry]
Name=Distortion
Exec=Distortion
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Distortion
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Flanger.desktop <<EOF
[Desktop Entry]
Name=Flanger
Exec=Flanger
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Flanger
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Panning.desktop <<EOF
[Desktop Entry]
Name=Panning
Exec=Panning
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Panning
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Parametric_EQ.desktop <<EOF
[Desktop Entry]
Name=Parametric EQ
Exec=Parametric\ EQ
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Parametric EQ
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Phaser.desktop <<EOF
[Desktop Entry]
Name=Phaser
Exec=Phaser
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Phaser
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Ping-Pong_Delay.desktop <<EOF
[Desktop Entry]
Name=Ping-Pong Delay
Exec=Ping-Pong\ Delay
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Ping-Pong Delay
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Pitch_Shift.desktop <<EOF
[Desktop Entry]
Name=Pitch Shift
Exec=Pitch\ Shift
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Pitch Shift
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Ring_Modulation.desktop <<EOF
[Desktop Entry]
Name=Ring Modulation
Exec=Ring\ Modulation
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Ring Modulation
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Robotization-Whisperization.desktop <<EOF
[Desktop Entry]
Name=Robotization-Whisperization
Exec=Robotization-Whisperization
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Robotization-Whisperization
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Template_Frequency_Domain.desktop <<EOF
[Desktop Entry]
Name=Template Frequency Domain
Exec=Template\ Frequency\ Domain
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Template Frequency Domain
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Template_Time_Domain.desktop <<EOF
[Desktop Entry]
Name=Template Time Domain
Exec=Template\ Time\ Domain
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Template Time Domain
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Tremolo.desktop <<EOF
[Desktop Entry]
Name=Tremolo
Exec=Tremolo
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Tremolo
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/Vibrato.desktop <<EOF
[Desktop Entry]
Name=Vibrato
Exec=Vibrato
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Vibrato
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF


cat > %{buildroot}%{_datadir}/applications/Wah-Wah.desktop <<EOF
[Desktop Entry]
Name=Wah-Wah
Exec=Wah-Wah
Icon=/usr/share/pixmaps/audio-effects
Comment=Audio Effects Wah-Wah
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF


for Files in %{buildroot}%{_datadir}/applications/*.desktop
do
  desktop-file-install                         \
    --dir=%{buildroot}%{_datadir}/applications \
    $Files
done

%check
for Files in %{buildroot}%{_datadir}/applications/*.desktop
do
  desktop-file-validate $Files
done

%files
%doc README.md
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Tue Aug 09 2022 Yann Collette <ycollette.nospam@free.fr> - 2.3.4-4
- update to 2.3.4-4

* Tue Jun 14 2022 Yann Collette <ycollette.nospam@free.fr> - 2.3.3-4
- update to 2.3.3-4

* Sat Jun 11 2022 Yann Collette <ycollette.nospam@free.fr> - 2.3.2-4
- update to 2.3.2-4

* Fri Aug 20 2021 Yann Collette <ycollette.nospam@free.fr> - 2.3.1-4
- add LV2 version

* Wed Aug 18 2021 Yann Collette <ycollette.nospam@free.fr> - 2.3.1-2
- update to 2.3.1-2

* Mon Oct 26 2020 Yann Collette <ycollette.nospam@free.fr> - 2.2.4-2
- fix install

* Sat Oct 24 2020 Yann Collette <ycollette.nospam@free.fr> - 2.2.4-1
- Initial spec file
