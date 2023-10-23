# Tag: Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    testsignal.lv2
Version: 0.6.5
Release: 1%{?dist}
Summary: LV2 Test Signal Generator
License: GPL-2.0-or-later
URL:     https://github.com/x42/testsignal.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/testsignal.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: lv2-devel

%description
testsignal.lv2 is an audio-plugin for generating test-signals in LV2 format.

It has 9 operation modes:
- Sine Wave 1kHz
- Square Wave 1kHz
- Sine Sweep 20Hz to 20KHz (at most to samplerate / 2) in 10 seconds
- Uniform White Noise
- Gaussian Shaped White Noise
- Pink Noise
- Impulses (1 sample spike) 100Hz, 0dBFS
- Impulses (1 sample spike) 1Hz, 0dBFS
- Impulses (1 sample spike) 5s (0.2Hz), 0dBFS

The signal level can be varied between -24dBFS and -9dBFS and defaults to -18dBFS.
- For sine level defines the peak-signal (RMS is identical)
- For square-wave generator the level defines the peak-signal (RMS is +3dB)
- For uniform white noise, the level defines the absolute peak
  (RMS is about -1.8dB below peak)
- For Gaussian shaped white noise and pink-noise, the level sets the RMS
  (peak is unlimited, though usually less than +12dB above RMS)

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"
%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%install

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Fri May 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.5-1
- update to 0.6.5-1

* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.4-1
- update to 0.6.4-1

* Sun Nov 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- update to 0.6.3-1

* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-1
- Initial spec file
