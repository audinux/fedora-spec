# Status: active
# Tag: Sequencer, Modular
# Type: Standalone
# Category: Sequencer

%global commit0 460fb1eb1d2c07265a986a7a20c4e040cfc1e916
%global debug_package %{nil}

Name: flow
Version: 0.0.1
Release: 1%{?dist}
Summary: Polyphonic Modular Additive Synthesizer
License: Apache-2.0
URL: https://github.com/eclab/flow
ExclusiveArch: x86_64 aarch64
BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/eclab/flow/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz
Source1: flow.sh

BuildRequires: gcc
BuildRequires: make
BuildRequires: java-latest-openjdk-devel

%description
Flow is a fully-modular multitimbral and polyphonic additive software synthesizer written in pure Java.
It runs on MacOS, Linux, and Windows.
I have used it to play individual patches and to play many simultaneous patches for a full song controlled
over MIDI via a DAW.
Flow has almost 70 modules of different shapes and sizes, and currently supports up to 32 voices at up
to 256 partials and 44.1KHz with a rate of one new partial update every 32 samples. Flow is a very
computationally expensive program and will keep your laptop quite warm and your fan busy. You need to have
some fairly good hardware to run Flow at full blast successfully (for reference, Flow was developed on a
2.8Ghz i7 2015 Macbook Pro Retina). There are options for reducing Flow's footprint (such as reducing the
number of voices or partials).

%prep
%autosetup -n %{name}-%{commit0}

%build

make

cat > MANIFEST.MF <<EOF 
Manifest-Version: 1.0
Main-Class: flow.Flow
Class-Path: /usr/share/java/flow/coremidi4j-1.5.jar /usr/share/java/flow/json.jar
EOF

jar cfm flow.jar MANIFEST.MF $(find . -name "*.class") $(find . -name "*.png")

%install

install -m755 -d %{buildroot}/%{_bindir}/
install -m755 %{SOURCE1} %{buildroot}/%{_bindir}/jflow

install -m755 -d %{buildroot}/%{_datadir}/java/flow/
install -m644 libraries/coremidi4j-1.5.jar %{buildroot}/%{_datadir}/java/flow/
install -m644 libraries/json.jar           %{buildroot}/%{_datadir}/java/flow/
install -m644 flow.jar                     %{buildroot}/%{_datadir}/java/flow/

install -m755 -d    %{buildroot}/%{_datadir}/flow/
cp -ra docs         %{buildroot}/%{_datadir}/flow/
cp -ra flow/patches %{buildroot}/%{_datadir}/flow/

%files
%doc README.md
%license LICENSE
%{_bindir}/jflow
%{_datadir}/java/flow/*
%{_datadir}/flow/docs/*
%{_datadir}/flow/patches/*

%changelog
* Thu Sep 10 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial spec
