# Status: active
# Tag: Synthesizer
# Type: Standalone
# Category: Synthesizer

%global banks_commit0 c5c912131b31df5fdf372d2f06a25aaf2375837f

Name: zyn-fusion
Version: 3.0.6
Release: 1%{?dist}
Summary: The Zyn-Fusion synthesizer
License: GPL-2.0-or-later
URL: https://github.com/mruby-zest/mruby-zest-build
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./zest-source.sh <TAG>
#        ./zest-source.sh 3.0.6
#        ./zest-source.sh pugl-2026 -> at commit b02bf5434e63518c09b7cd057422cec4bf5194d8

Source0: mruby-zest-build.tar.gz
Source1: https://github.com/zynaddsubfx/instruments/archive/%{banks_commit0}.tar.gz#/zest-banks-%{version}.tar.gz
Source2: zest-source.sh
Patch0: zest-0001-set-qml-path.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: rubygem-rake
BuildRequires: libuv-devel
BuildRequires: mesa-libGL-devel

%description
The Zyn-Fusion synthesizer

%prep
%autosetup -p1 -n mruby-zest-build

tar xvfz %{SOURCE1}

%build

%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 zest %{buildroot}/%{_bindir}/

ln -s /usr/bin/zest %{buildroot}/usr/bin/zyn-fusion

install -m 755 -d %{buildroot}/%{_libdir}/
install -m 755 libzest.so %{buildroot}/%{_libdir}/

install -m 755 -d %{buildroot}/%{_datadir}/bash-completion/completions/
install -m 644 completions/zyn-fusion %{buildroot}/%{_datadir}/bash-completion/completions/

install -m 755 -d %{buildroot}/%{_datadir}/zyn-fusion/
cp -r instruments-%{banks_commit0}/banks instruments-%{banks_commit0}/examples %{buildroot}/%{_datadir}/zyn-fusion/

install -m 755 -d %{buildroot}/%{_datadir}/zyn-fusion/qml/
cp -a src/mruby-zest/example/* %{buildroot}/%{_datadir}/zyn-fusion/qml/

%files
%doc README.adoc contributing.adoc
%license LICENSE
%{_bindir}/*
%{_libdir}/*
%{_datadir}/zyn-fusion/qml/*
%{_datadir}/zyn-fusion/banks/*
%{_datadir}/zyn-fusion/examples/*
%{_datadir}/bash-completion/completions/*

%changelog
* Tue Jun 02 2026 Yann Collette <ycollette.nospam@free.fr> - 3.0.6-1
- initial version of the spec
