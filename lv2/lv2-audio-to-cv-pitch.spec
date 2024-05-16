# Tag: Audio, Tool
# Type: Plugin, LV2
# Category: Audio, Tool

Name: lv2-audio-to-cv-pitch
Version: 0.1
Release: 1%{?dist}
Summary: Plugin that converts audio to CV pitch (1 volt per Octave)
License: GPL-3.0-or-later
URL: https://github.com/BramGiesen/audio-to-cv-pitch-lv2
ExclusiveArch: x86_64 aarch64

# Usage: ./audio-to-cv-pitch-source.sh <TAG>
#        ./audio-to-cv-pitch-source.sh 27f5a5211ce04159016883870ff51425ee5b49e6

Source0: audio-to-cv-pitch-lv2.tar.gz
Source1: audio-to-cv-pitch-source.sh

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel

%description
Plugin that converts audio to CV pitch (1 volt per Octave)

%prep
%autosetup -n audio-to-cv-pitch-lv2

%build

%set_build_flags
%make_build SKIP_STRIPPING=true BASE_OPTS="$CXXFLAGS"

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra bin/* %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Thu Oct 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial creation
