# Tag: Editor, MIDI
# Type: Standalone
# Category: DAW, MIDI

Name: midieditor
Version: 3.3.2
Release: 1%{?dist}
Summary: Provides an interface to edit, record, and play Midi data
URL: https://github.com/markusschwenk/midieditor
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/markusschwenk/midieditor/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-linguist
BuildRequires: alsa-lib-devel
BuildRequires: libsndfile-devel
BuildRequires: desktop-file-utils

%description
MidiEditor is a free software providing an interface to edit,
record, and play Midi data.

The editor is able to open existing Midi files and modify their content.
New files can be created and the user can enter his own composition by
either recording Midi data from a connected Midi device (e.g., a digital
piano or a keyboard) or by manually creating new notes and other Midi events.
The recorded data can be easily quantified and edited afterwards using MidiEditor.

%prep
%autosetup -n %{name}-%{version}

sed -i -e "/Version/d" packaging/unix/midieditor/MidiEditor.desktop
sed -i -e "s/\.png//g" packaging/unix/midieditor/MidiEditor.desktop

%build

%set_build_flags
export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`

%qmake_qt5 midieditor.pro
%make_build

%install

%make_install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 MidiEditor %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/
install -m 644 midieditor.ico %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/%{name}.ico

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
install -m 644 packaging/unix/midieditor/logo48.png %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

install -m 755 -d %{buildroot}/%{_datadir}/midieditor/manual/
cp -ra manual/* %{buildroot}/%{_datadir}/midieditor/manual/

install -m 755 -d %{buildroot}/%{_datadir}/midieditor/metronome/
cp run_environment/metronome/* %{buildroot}/%{_datadir}/midieditor/metronome/

install -m 755 -d %{buildroot}/%{_datadir}/midieditor/examples/
cp run_environment/mozart_turkish_march.mid %{buildroot}/%{_datadir}/midieditor/examples/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 packaging/unix/midieditor/MidiEditor.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop

# install polyphon.desktop properly.
desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.ico
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/midieditor/
%{_datadir}/midieditor/manual/*
%{_datadir}/midieditor/examples/*
%{_datadir}/midieditor/metronome/*

%changelog
* Tue Sep 13 2022 Yann Collette <ycollette.nospam@free.fr> - 3.3.2-1
- Initial spec file
