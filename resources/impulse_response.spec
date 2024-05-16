# Tag: Presets
# Type: Presets
# Category: Plugin

Summary: Impulse responses for various cabinet
Name: impulse-response
Version: 1.0.1
Release: 2%{?dist}
License: GPL-2.0-or-later AND GPL-3.0-only
URL: https://musical-artifacts.com/artifacts/252
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Amp
Source0: https://musical-artifacts.com/artifacts/252/650-Assorted-Cabinet-Impulses.zip
# Reverb
Source1: https://www.voxengo.com/files/impulses/IMreverbs.zip

BuildArch: noarch

BuildRequires: unzip

%description
Impulse responses for various cabinet:
- Amplifier impulse responses from musical artifacts
- Reverb impulse responses (IMReverbs) from voxengo

%prep

%install

rm -rf IR_files

mkdir -p IR_files/amp
cd IR_files/amp
unzip %{SOURCE0}
cd ../..
mkdir -p IR_files/IMReverbs
cd IR_files/IMReverbs
unzip %{SOURCE1}
cd ../..

mkdir -p %{buildroot}/%{_datadir}/IR/
cp -r IR_files/* %{buildroot}/%{_datadir}/IR/

%files
%{_datadir}/IR/

%changelog
* Tue Oct 05 2021 Yann Collette <ycollette dot nospam at free.fr> 1.0.1-2
- Add some reverb IR

* Mon Oct 04 2021 Yann Collette <ycollette dot nospam at free.fr> 1.0.0-2
- fix for Fedora 35

* Sun May 17 2020 Yann Collette <ycollette dot nospam at free.fr> 1.0.0-1
- initial spec file
