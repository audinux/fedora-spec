# Status: active
# Tag: Effect
# Type: LADSPA
# Category: Audio, Effect

%global commit0 fff6ef29c52709588cdd3003d64690470cf64646

Name: ladspa-twk
Version: 0.0.1
Release: 1%{?dist}
Summary: A collection of ladspa plugins
License: GPL-3.0+
URL: https://github.com/TimKrause2/twk-ladspa-plugins
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/TimKrause2/twk-ladspa-plugins/archive/%{commit0}.zip#/%{name}-%{commit0}.zip

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: ladspa-devel

%description

A collection of ladspa plugins:
 * 5801 Compressor/Expandor
 * 5802 DC remove
 * 5803 Delay
 * 5804 Distortion
 * 5805 Impulse train generator
 * 5806 Voice control impulse train generator
 * 5807 All pass filter with LFO control of delay interval
 * 5808 Bandpass filter with LFO control of frequency
 * 5809 Bandpass filter bank, 5 filters, with LFO control of frequency
 * 5810 Delay with LFO control of interval
 * 5811 Bandpass filter bank, 5 filters, with random control of frequency
 * 5812 Linear prediction based vocoder
 * 5813 Phaser based on digital integrator
 * 5814 Phaser based on all pass filters
 * 5815 RBJ band pass filter with bandwidth control
 * 5816 RBJ band pass filter with Q control
 * 5817 RBJ high pass filter with Q control
 * 5818 RBJ high pass filter bank with Q control
 * 5819 RBJ high shelf filter
 * 5820 RBJ low pass filter with Q control
 * 5821 RBJ low pass filter bank with Q control
 * 5822 RBJ low shelf filter
 * 5823 RBJ peaking EQ
 * 5824 Adjustable reverb
 * 5825 Sine wave generator
 * 5826 Butterworth low pass filter
 * 5827 Butterworth high pass filter
 * 5828 Butterworth band pass filter
 * 5829 Butterworth band stop filter
 * 5830 Elliptical low pass filter
 * 5831 Elliptical high pass filter
 * 5832 Elliptical band pass filter
 * 5833 Elliptical band stop filter
 * 5834 Pitch Shifter

RBJ = Robert Bristow-Johnson of Audio-EQ-Cookbook.txt

%prep
%autosetup -n twk-ladspa-plugins-%{commit0}

sed -i -e "/CFLAGS=/d" Makefile
sed -i -e "s|\$(PLUGIN_OBJECTS)|\$(CFLAGS) \$(PLUGIN_OBJECTS)|g" Makefile

%build

%set_build_flags

export CFLAGS="-fPIC -Ifad $CFLAGS"

%make_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/ladspa/
install -m 755 twk.so %{buildroot}/%{_libdir}/ladspa/

%files
%doc README.md Cookbook.txt Audio-EQ-Cookbook.txt
%license COPYING
%{_libdir}/ladspa/*

%changelog
* Wed Dec 03 2025 Yann Collette <ycollette dot nospam at free.fr> 0.0.1-1
- initial spec
