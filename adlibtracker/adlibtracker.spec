# Status: active
# Tag: Tracker, Jack, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name: adlibtracker
Version: 2.4.25
Release: 1%{?dist}
Summary: Adlib Tracker II is, dare we say, the most userfriendly tracker aimed for the OPL3 FM-chip
License: GPL-3.0-or-later
URL: https://adlibtracker.net
ExclusiveArch: x86_64 aarch64

Vendor: Audinux
Distribution: Audinux

Source0: https://adlibtracker.net/files/at2_sourcecode_06-02-2026.zip

BuildRequires: fpc gcc
BuildRequires: make
BuildRequires: sdl12-compat-devel
BuildRequires: sdl12-compat-static
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: desktop-file-utils

%description
Welcome to the official Adlib Tracker II website! Here you'll find the latest info on subz3ro's finest FM-tracker.
This will in time be the place to discover how to make most use of the OPL3-chip and a place to share your interest
in FM-synthesis with other users.
Adlib Tracker II is, dare we say, the most userfriendly tracker aimed for the OPL3 FM-chip, and is full of advanced
features to simplify your task of making the most of your Adlib-tunes. Supporting 4 operator instruments,
percussion mode, a wide selection of importable song- and instrument types and - maybe foremost - an advanced
macro editor that can really push the FM-chip to the limit.
If you're lucky enough to have an old PC machine lying around with a Sound Blaster compatible card - or a brand
new computer that can simulate it - don't hesitate to install and get grooving with this ultimate FM-tool of yours!
Feel free to browse these pages to find out more about Adlib Tracker II and see what you can do with it. Enjoy!

%prep
%autosetup -n git

sed -i -e "s/-O2 -XXs -Ccpascal/-g -va -O2 -XXs -Ccpascal/g" makefile

%build

%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 adtrack2 %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/adlibtracker/
cp -ra package/instr %{buildroot}/%{_datadir}/adlibtracker/
cp -ra package/modules %{buildroot}/%{_datadir}/adlibtracker/
install -m 644 package/ver/sdl/adtrack2.docx %{buildroot}/%{_datadir}/adlibtracker/
install -m 644 package/ver/sdl/adtrack2.ini %{buildroot}/%{_datadir}/adlibtracker/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp package/ver/sdl/linux/adtrack2.png %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=adlibtracker
Exec=adtrack2
Icon=adtrack2
Comment=Adlib Tracker II is, dare we say, the most userfriendly tracker aimed for the OPL3 FM-chip
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc readme-sdl.txt
%license lgpl-2.1.txt
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/adlibtracker/*
%{_datadir}/pixmaps/*

%changelog
* Sat Sep 05 2026 Yann Collette <ycollette dot nospam at free dot fr> 2.4.25-1
- initial spec
