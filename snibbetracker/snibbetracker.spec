# Status: active
# Tag: Tracker, Alsa
# Type: Standalone
# Category: Audio, Sequencer

%global commit0 b50c7a46b30589e833aab47fee3ee7bf4c33eb0a

Name: snibbetracker
Version: 1.1.1
Release: 1%{?dist}
Summary: Fakebit music tracker
License: MIT
URL: https://github.com/linuxmao-org/snibbetracker
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/linuxmao-org/snibbetracker/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: SDL2-devel
BuildRequires: desktop-file-utils

%description
snibbetracker is a fakebit tracker written in C using SDL2 that I began working
on in 2014 to learn DSP programming. As I do not have time to work on it anymore,
I decided to release the source so that someone could take over if they wanted.

%prep
%autosetup -n %{name}-%{commit0}

%build

cd res/linux/

%make_build

%install

cd res/linux/

%make_install PREFIX=/usr

cd ..

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Exec=%{name}
Icon=%{name}
Comment=%{name} tracker
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/apps/16x16
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/apps/32x32
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/apps/128x128
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/apps/256x256
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/apps/512x512

cp -a \[IconName\].iconset/*16x16.png   %{buildroot}/%{_datadir}/icons/hicolor/apps/16x16/%{name}.png
cp -a \[IconName\].iconset/*32x32.png   %{buildroot}/%{_datadir}/icons/hicolor/apps/32x32/%{name}.png
cp -a \[IconName\].iconset/*128x128.png %{buildroot}/%{_datadir}/icons/hicolor/apps/128x128/%{name}.png
cp -a \[IconName\].iconset/*256x256.png %{buildroot}/%{_datadir}/icons/hicolor/apps/256x256/%{name}.png
cp -a \[IconName\].iconset/*512x512.png %{buildroot}/%{_datadir}/icons/hicolor/apps/512x512/%{name}.png

mkdir -p %{buildroot}/%{_datadir}/%{name}/
mv %{buildroot}/%{_datadir}/lundstroem/snibbetracker/demos %{buildroot}/%{_datadir}/%{name}/demos
rm -rf %{buildroot}/%{_datadir}/lundstroem/

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/icons/*
%{_datadir}/%{name}/demos/*
%{_datadir}/applications/*

%changelog
* Wed Sep 10 2025 Yann Collette <ycollette dot nospam at free dot fr> - 1.1.1-1
- Initial version of the package
