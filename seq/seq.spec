# Status: active
# Tag: Sequencer
# Type: Standalone
# Category: Sequencer

%global commit0 9eabbb38891948edfc9625e328cca96a6369f4a5
%global debug_package %{nil}

Name: seq
Version: 0.0.1
Release: 1%{?dist}
Summary: A Unique Modular and Hierarchical MIDI Sequencer
License: Apache-2.0
URL: https://github.com/eclab/seq
ExclusiveArch: x86_64 aarch64
BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/eclab/seq/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz
Source1: seq.sh

BuildRequires: gcc
BuildRequires: make
BuildRequires: java-latest-openjdk-devel

%description
A Modular, Hierarchical Music Sequencer (Version 10) By Sean Luke (sean@cs.gmu.edu)
With Help from Filippo Carnovalini (filippo.carnovalini@vub.be) and Cesar Liendo (cliendo@gmu.edu)
Copyright 2024-2026 by Sean Luke and George Mason University

Related projects:
- Edisyn, a patch editor toolkit with sophisticated exploration tools.
- Flow, a fully-modular, polyphonic, additive software synthesizer.
- Gizmo, an Arduino-based MIDI Swiss Army knife.
- Arduino Firmware (oscillators, modulators, etc.) for the AE Modular Grains module. Includes an ultralight but full-featured MIDI library for small microcontrollers.
- Computational Music Synthesis, an open-content book on building software synthesize

%prep
%autosetup -n %{name}-%{commit0}

%build

make

cat > MANIFEST.MF <<EOF 
Manifest-Version: 1.0
Main-Class: seq.Seq
Class-Path: /usr/share/java/seq/coremidi4j-1.6.jar /usr/share/java/seq/flatlaf-3.4.1.jar /usr/share/java/seq/json.jar
EOF

jar cfm seq.jar MANIFEST.MF $(find . -name "*.class") $(find . -name "*.png")

%install

install -m755 -d %{buildroot}/%{_bindir}/
install -m755 %{SOURCE1} %{buildroot}/%{_bindir}/jseq

install -m755 -d %{buildroot}/%{_datadir}/java/seq/
install -m644 libraries/coremidi4j-1.6.jar %{buildroot}/%{_datadir}/java/seq/
install -m644 libraries/flatlaf-3.4.1.jar  %{buildroot}/%{_datadir}/java/seq/
install -m644 libraries/json.jar           %{buildroot}/%{_datadir}/java/seq/
install -m644 seq.jar                      %{buildroot}/%{_datadir}/java/seq/

install -m755 -d %{buildroot}/%{_datadir}/seq/
cp -ra docs     %{buildroot}/%{_datadir}/seq/
cp -ra drumsets %{buildroot}/%{_datadir}/seq/
cp -ra songs    %{buildroot}/%{_datadir}/seq/

%files
%doc README.md
%license LICENSE
%{_bindir}/jseq
%{_datadir}/java/seq/*
%{_datadir}/seq/docs/*
%{_datadir}/seq/drumsets/*
%{_datadir}/seq/songs/*

%changelog
* Fri Jul 10 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial spec
