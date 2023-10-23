# Tag:
# Type:
# Caterogy: Presets

Name:    BespokeSynth-examples
Version: 1.0.0
Release: 7%{?dist}
Summary: Examples for BespokeSynth
License: GPL-2.0-or-later
URL:     https://github.com/initialed85/bespoke-synth-jams

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/initialed85/bespoke-synth-jams/archive/refs/heads/master.zip#/%{name}-%{version}.zip

BuildArch: noarch

%description
Examples for BespokeSynth:
- Jam! examples frome the repository bespoke-synth-jams

%prep
%autosetup -n bespoke-synth-jams-master

%build

%install

install -m 755 -d %{buildroot}/%{_datadir}/BespokeSynth/examples/Jam/
cp -r *.bsk  %{buildroot}/%{_datadir}/BespokeSynth/examples/Jam/

%files
%doc README.md
%{_datadir}/*

%changelog
* Fri Oct 22 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
