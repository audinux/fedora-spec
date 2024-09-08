# Status: active
# Tag: Editor, Audio
# Type: Standalone
# Category: Audio, Sampler, Sequencer

Name: linux-show-player
Version: 0.6.4
Release: 1%{?dist}
Summary: A Cue player designed for stage productions
License: GPL-2.0-or-later
URL: https://github.com/FrancescoCeruti/linux-show-player
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/FrancescoCeruti/linux-show-player/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
#BuildRequires: python-jack-client
#BuildRequires: python3-mido
#BuildRequires: python3-qt5-base
#BuildRequires: python3-sortedcontainers
#BuildRequires: python3-rtmidi
#BuildRequires: python3-pyliblo
#BuildRequires: python3-alsa
BuildRequires: pyproject-rpm-macros
BuildRequires: alsa-lib-devel
BuildRequires: gobject-introspection-devel
BuildRequires: desktop-file-utils

Requires: python-jack-client
Requires: python3-mido
Requires: python3-qt5-base-gui
Requires: python3-sortedcontainers
Requires: python3-rtmidi
Requires: python3-pyliblo
Requires: python3-alsa

Requires: gstreamer1-plugins-good
Requires: gstreamer1-libav

%generate_buildrequires
%pyproject_buildrequires

%description
Linux Show Player (LiSP) - Sound player designed for stage productions.

%prep
%autosetup -n %{name}-%{version}

%build

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files onelogin

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Sun Sep 08 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.4-1
- update to version 0.6.4-1

* Sat Dec 25 2021 Yann Collette <ycollette.nospam@free.fr> - 0.5.3-1
- update to version 0.5.3-1

* Fri Mar 12 2021 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- Initial spec file
