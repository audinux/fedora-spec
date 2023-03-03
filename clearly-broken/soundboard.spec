# Tag: Sampler
# Type: Plugin, LV2, VST3
# Category: Audio, Effect

%global commit0 c2447333286dad81bdcd73a25e481c3bfdab58e3

Name: soundboard
Version: 0.0.1
Release: 1%{?dist}
Summary: Easy to use soundboard
License: GPLv2	
URL: https://github.com/clearly-broken-software/SoundBoard

# Usage: ./soundboard-source.sh <TAG>
# ./soundboard-source.sh c2447333286dad81bdcd73a25e481c3bfdab58e3

Source0: SoundBoard.tar.gz
Source1: soundboard-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: mesa-libGL-devel
BuildRequires: libsndfile-devel
BuildRequires: rubberband-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel
BuildRequires: lv2-devel
BuildRequires: desktop-file-utils

%description
Easy to use soundboard

%package -n vst-%{name}
Summary:  VST version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst-%{name}
VST version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n SoundBoard

%build
%set_build_flags
%make_build SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/SoundBoard.lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst/

install -m 755 -p bin/SoundBoard %{buildroot}%{_bindir}/
install -m 755 -p bin/SoundBoard-vst.so %{buildroot}%{_libdir}/vst/
cp -ra bin/SoundBoard.lv2/* %{buildroot}%{_libdir}/lv2/SoundBoard.lv2/

install -m 755 -d %{buildroot}/%{_datadir}/icons/%{name}/
install -m 644 -p SoundBoard.png %{buildroot}/%{_datadir}/icons/%{name}/

# Create some desktop files
install -m 755 -d %{buildroot}%{_datadir}/applications/

cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=SoundBoard
Comment=A Sampler Launcher
Exec=SoundBoard
Icon=SoundBoard
Terminal=false
Type=Application
Categories=Audio;
EOF

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%{_bindir}/*
%{_datadir}/icons/*
%{_datadir}/applications/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Tue Aug 02 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial spec file
