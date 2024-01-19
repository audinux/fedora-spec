# Tag: OSC
# Type: LADSPA
# Category: Audio, Synthesizer

Name: ladspa-omins
Version: 0.2.0
Release: 1%{?dist}
Summary: Omins is a collection of LADSPA plugins geared at modular synthesizers.
License: GPL-2.0+
URL: https://www.nongnu.org/om-synth/omins.html

Vendor:       Audinux
Distribution: Audinux

Source0: https://download.savannah.gnu.org/releases/om-synth/omins-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: ladspa-devel

%description
Omins is a collection of LADSPA plugins geared at modular synthesizers.
The name comes from Om, but these plugins are not Om specific in any way,
and Om does not require them. However most (not all) of them are only
really useful in modular systems.

%prep
%autosetup -n omins-%{version}

%build

%configure
%make_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/ladspa/
for Files in "src/.libs/*.so"
do
  install -m 755 $Files %{buildroot}/%{_libdir}/ladspa/
done

%files
%doc README AUTHORS ChangeLog
%license COPYING
%{_libdir}/ladspa

%changelog
* Mon Nov 28 2022 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-1
- initial spec
