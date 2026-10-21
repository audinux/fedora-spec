# Status: active
# Tag: Tracker
# Type: Standalone
# Category: Sequencer

%global debug_package %{nil}

%global commit0 86d2fe9bf4dfc90b8379c59d891a7c959ffa4285
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: piper
Version: 0.0.1
Release: 1%{?dist}
Summary: Mini modular tracker written in lua using love2d
License: GPL-2.0-or-later
URL: https://github.com/awlkak/piper
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/awlkak/piper/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: curl
BuildRequires: love

Requires: love

%description
Piper is a mini modular tracker in the spirit of BuzzTracker, Max/MSP, SunVox, PD, and a bunch of other
niche software, with a very simple, portable interface, and every synth & effect built as a lua plugin.
The idea is it runs anywhere, is open, and anybody can easily build for it.

%prep
%autosetup -n %{name}-%{commit0}

%build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cat > %{buildroot}/%{_bindir}/%{name} <<EOF
#!/bin/bash

exec /usr/bin/love /usr/share/piper/piper-%{version}-%{release}.love "$@"
EOF
chmod 755 %{buildroot}/%{_bindir}/%{name}

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/

mkdir tmp
cd tmp
tar xvfz %{SOURCE0}
cd %{name}-%{commit0}
zip -r %{name}-%{version}-%{release}.love .

cp %{name}-%{version}-%{release}.love %{buildroot}/%{_datadir}/%{name}/%{name}-%{version}-%{release}.love
cd ../..

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/examples/
install -m 644 songs/* %{buildroot}/%{_datadir}/%{name}/examples/

%files
%doc README.md
%{_bindir}/*
%{_datadir}/%{name}/piper-%{version}-%{release}.love
%{_datadir}/%{name}/examples/*

%changelog
* Wed Oct 21 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial spec
