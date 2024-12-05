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
BuildRequires: python3-setuptools
BuildRequires: python3-pip
BuildRequires: python3-wheel
BuildRequires: python3-poetry
BuildRequires: alsa-lib-devel
BuildRequires: gobject-introspection-devel
BuildRequires: desktop-file-utils

# Requires: python-jack-client
# Requires: ola
# Requires: artnet
# Requires: jack_sink

Requires: python3-qt5
Requires: python3-sortedcontainers
Requires: python3-rtmidi
Requires: python3-pyliblo
Requires: python3-alsa
Requires: python3-mido
Requires: python3-humanize
Requires: python3-falcon

Requires: gstreamer1-plugins-good
Requires: gstreamer1-libav

%description
Linux Show Player (LiSP) - Sound player designed for stage productions.

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s/mido = \"\^1.3\"/mido = \"\^1.2\"/g" pyproject.toml
# sed -i -e "s/falcon = \"\^3.0\"/falcon = \"\^4.0\"/g" pyproject.toml
# sed -i -e "s/humanize = \"\^4.8.0\"/humanize = \"\^4.0.0\"/g" pyproject.toml

sed -i -e "/pyqt5-qt5/d" pyproject.toml
sed -i -e "/falcon/d" pyproject.toml
sed -i -e "/humanize/d" pyproject.toml
sed -i -e "/python3-qt5/d" pyproject.toml
sed -i -e "/jack-client/d" pyproject.toml

#sed -i -e "s/pyqt5/python3-qt5/g" pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files lisp

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/linux-show-player

%changelog
* Sun Sep 08 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.4-1
- update to version 0.6.4-1

* Sat Dec 25 2021 Yann Collette <ycollette.nospam@free.fr> - 0.5.3-1
- update to version 0.5.3-1

* Fri Mar 12 2021 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- Initial spec file
