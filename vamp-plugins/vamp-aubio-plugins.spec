# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: vamp-aubio-plugins
Version: 0.5.1
Release: 2%{?dist}
Summary:  aubio plugins for Vamp
License: GLPv2
URL: https://github.com/aubio/vamp-aubio-plugins

Vendor:       Audinux
Distribution: Audinux

Source0: https://aubio.org/pub/vamp-aubio-plugins/vamp-aubio-plugins-%{version}.tar.bz2

BuildRequires: gcc gcc-c++ make
BuildRequires: vamp-plugin-sdk-devel
BuildRequires: aubio-devel

%description
A set of Vamp plugins for audio feature extraction using the aubio library.

This set includes the following plugins:

* Aubio Beat Tracker
    Time → Tempo
    Estimate the musical tempo and track beat positions.
* Aubio Mel-frequency Band Energy Detector
    Low Level Features
    Computes Energy in each Mel-Frequency Bands.
* Aubio Mfcc Detector
    Low Level Features
    Computes Mel-Frequency Cepstrum Coefficients.
* Aubio Note Tracker
    Notes
    Estimate note onset positions, pitches and durations.
* Aubio Onset Detector
    Time → Onsets
    Estimate note onset times.
* Aubio Pitch Detector
    Pitch
    Track estimated note pitches.
* Aubio Silence Detector
    Low Level Features
    Detect levels below a certain threshold.
* Aubio Spectral Descriptor
    Low Level Features
    Computes spectral descriptor.

%prep
%autosetup

sed -i -e "s/-Wall -Wextra -O3.*/\$(CFLAGS) -fPIC/g" Makefile.linux
sed -i -e "s|\./contrib/aubio/build/src/libaubio\.a|-laubio|g" Makefile.linux

%build

%set_build_flags

%make_build -f Makefile.linux

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 vamp-aubio.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 vamp-aubio.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 vamp-aubio.n3  %{buildroot}/%{_libdir}/vamp/

%files
%license COPYING
%doc README.md
%{_libdir}/vamp/vamp-aubio.*

%changelog
* Fri Jul 22 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-2
- update to 0.5.1-2

* Sat Jan 08 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- Initial spec file

