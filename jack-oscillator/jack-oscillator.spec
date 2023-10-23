%global commit0 31c6bfa81f223ccc5d840effbf15881907eadad4

Summary: Single oscillator with traditional waveforms for JACK
Name:    jack-oscillator
Version: 0.1
Release: 1%{?dist}
License: GPL-3.0-only
URL:     https://github.com/michelesr/jack-oscillator

Source0: https://github.com/michelesr/jack-oscillator/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc
BuildRequires: make
BuildRequires: jack-audio-connection-kit-devel

%description
Single oscillator synthesizer with traditional waveforms for
JACK (Jack Audio Connection Kit)
This is a single-oscillator lightweight synthesizer, with
traditional waves (sine, square, sawtooth, triangle). You can
select the form, amplitude and envelope of the wave.

%prep

%autosetup -n %{name}-%{commit0}

sed -i -e "s|-O2|-O2 \$(DEPCFLAGS)|g" Makefile
sed -i -e "s|-g|-g \$(DEPLDFLAGS)|g" Makefile

%build

%set_build_flags
export DEPLDFLAGS="$LDFLAGS"
export DEPCFLAGS="$CFLAGS"

%make_build bin/simple_osc

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp bin/simple_osc %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
* Wed Jul 19 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- initial build

