# Tag: Editor
# Type: Standalone, IDE
# Category: Programming, Audio

Name:    rtcqs
Version: 0.5.2
Release: 1%{?dist}
Summary: rtcqs is a Python utility to setup real time parameters for low latency audio
License: Creative Commons Attribution-ShareAlike 4.0 International Public License
URL: https://codeberg.org/rtcqs/rtcqs

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeberg.org/rtcqs/rtcqs/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pip
BuildRequires: python3-tkinter
BuildRequires: desktop-file-utils

Requires: python3-tkinter
Requires: python3-pyside2

%description
rtcqs is a Python utility to analyze your system and detect possible bottlenecks
that could have a negative impact on the performance of your system when working
with Linux audio.

%prep
%autosetup -n %{name}

%install

pip3 install --root=%buildroot .

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
cp rtcqs_logo.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
cp rtcqs.desktop %{buildroot}/%{_datadir}/applications/

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{name}/__pycache__/*
%{_bindir}/%{name}
%{_bindir}/%{name}_gui
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-*.dist-info
%{python3_sitelib}/%{name}/*.py
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*

%changelog
* Sun Nov 20 2022 Yann Collette <ycollette dot nospam at free.fr> 0.5.2-1
- initial release of the spec file
