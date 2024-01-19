# Tag: Effect, Equalizer
# Type: LADSPA
# Category: Audio, Effect

Name: ladspa-t5-plugins
Version: 1.8
Release: 1%{?dist}
Summary: LADSPA filter plugins
License: GPL-2.0+
URL: https://gitlab.com/t-5/ladspa-t5-plugins

Vendor:       Audinux
Distribution: Audinux

Source: https://gitlab.com/t-5/ladspa-t5-plugins/-/archive/%{version}/ladspa-t5-plugins-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson
BuildRequires: ladspa-devel

%description
This plugin collection is intended for use with Pulseaudio Parametric Equalizer
and will be extended to support building multi-way loudspeaker crossovers in
pulseaudio (look at Pulseaudio Crossover Rack).

%prep
%autosetup -n %{name}-%{version}

%build

cd src
%meson
%meson_build

%install

cd src
%meson_install

mkdir %{buildroot}%{_libdir}/ladspa
mv %{buildroot}%{_libdir}/*.so %{buildroot}%{_libdir}/ladspa/

%files
%doc README.md
%{_libdir}/ladspa

%changelog
* Sat Jul 24 2021 Yann Collette <ycollette dot nospam at free.fr> 1.8-1
- initial version
