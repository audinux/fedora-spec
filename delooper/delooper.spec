# Tag: Loop
# Type: Standalone
# Category: Tool, Audio

%global commit0 0ff9ac414d6c7daa3ef494d43524b9e1c9e3f7f5

Name:    delooper
Version: 0.0.1
Release: 1%{?dist}
Summary: Audio Looper
URL:     https://github.com/sonejostudios/DeLooper
License: GPL-3.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/sonejostudios/DeLooper/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: pkgconfig(jack)
BuildRequires: faust-tools
BuildRequires: qt5-qtbase-devel
BuildRequires: alsa-lib-devel

%description
Sample-accurate Looper/Delay with free mode and midi-clock sync mode.

%prep

%autosetup -n DeLooper-%{commit0}

%build

faust2jaqt -midi DeLooper.dsp

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp DeLooper %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
* Thu Oct 19 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
