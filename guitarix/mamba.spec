# Tag: MIDI
# Type: Standalone
# Category: Audio, Sequencer

Name: mamba
Version: 2.6
Release: 4%{?dist}
Summary: Virtual Midi Keyboard for Jack Audio Connection Kit
License: BSD
URL: https://github.com/brummer10/Mamba

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/brummer10/Mamba/releases/download/v%{version}/Mamba_%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(jack)
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel
BuildRequires: libsmf-devel
BuildRequires: fluidsynth-devel
BuildRequires: alsa-lib-devel
BuildRequires: libsndfile-devel
BuildRequires: vim-common
BuildRequires: desktop-file-utils

%description
Mamba is not only a Virtual MIDI keyboard, it's also a MIDI looper.
It allow you to record, for example a bass loop on one channel and
then play along on a other channel with a piano or whatever.

You could save your loops to MIDI files if you wish, in any case,
Mamba save your last record and load it on the next start on default.

Mamba is also a MIDI visualizer, it shows not only what you play,
it shows as well incoming events. It also allow you to load MIDI files,
play them in loop and show the output on the keyboard. You could select
which channel you would monitor on the keyboard.
You could as well monitor all channels at once.

Mamba includes also support by fluidsynth,
you could load a soundfont and directly play along.

Mamba will keep it's settings, so once a soundfont is loaded,

on the next start you could just play along with the keyboard.
You could load a new soundfont at any time. You could as well
exit fluidsynth to use Mamba as plain Virtual MIDI keyboard
with the synth of your choice.

%prep
%autosetup -n Mamba_%{version}

%build

%set_build_flags

export CXXFLAGS=`echo $CXXFLAGS | sed -e "s|-Werror=format-security||g"`
export CFLAGS=`echo $CFLAGS | sed -e "s|-Werror=format-security||g"`

%make_build

%install

%make_install

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=X-Jack \
        --dir %{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/Mamba.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/Mamba.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/Mamba.desktop
%{_datadir}/pixmaps/Mamba.svg

%changelog
* Sat Mar 23 2024 Yann Collette <ycollette.nospam@free.fr> - 2.6-4
- update to 2.6-4

* Fri May 19 2023 Yann Collette <ycollette.nospam@free.fr> - 2.5-4
- update to 2.5-4

* Thu May 18 2023 Yann Collette <ycollette.nospam@free.fr> - 2.4-4
- update to 2.4-4

* Tue Apr 19 2022 Yann Collette <ycollette.nospam@free.fr> - 2.3-4
- update to 2.3-4

* Sat Apr 17 2021 Yann Collette <ycollette.nospam@free.fr> - 2.2-4
- update to 2.2-4

* Sat Jan 9 2021 Yann Collette <ycollette.nospam@free.fr> - 2.1-4
- update to 2.1-4

* Sat Dec 19 2020 Yann Collette <ycollette.nospam@free.fr> - 2.0-4
- update to 2.0-4

* Tue Nov 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.9-4
- update to 1.9-4

* Mon Nov 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.8-4
- update to 1.8-4

* Fri Nov 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.7-4
- update to 1.7-4

* Mon Nov 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.7-3
- update to 1.7-3

* Mon Nov 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.7.0-2
- update to 1.7.0-2

* Tue Oct 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.0-2
- fix description, license and missing file

* Sat Oct 10 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.0-1
- update to 1.6.0-1

* Sat Sep 19 2020 Yann Collette <ycollette.nospam@free.fr> - 1.5.0-1
- update to 1.5.0-1

* Sun Sep 6 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-1
- update to 1.4.0-1

* Sat Aug 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- Initial spec file
