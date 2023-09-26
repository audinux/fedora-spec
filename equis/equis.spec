%define commit0 37b46ef90413a593d87a7e3351c08f1e23e48772

Name:    equis
Version: 0.0.1
Release: 1%{?dist}
Summary: The hackable DJ Mixer inspired by the playdifferently model 1
License: GPL-3.0-or-later
URL:     https://codeberg.org/obsoleszenz/equis

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeberg.org/obsoleszenz/EQUIS/archive/main.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: rust cargo
BuildRequires: jack-audio-connection-kit-devel

%description
This is a 8 Channel DJ Mixer built on top of JACK. It's EQ is inspired
by the Playdifferently Model1 and offers per channel a highpass, lowpass
and sculpt eq. Two channels can be used as send/return channels for effects.
Also you can assign every channel to one of two SubFilters that are
modeled after the Xone:96 DUAL VCF Filters. EQUIS offers 2 seperate CUE
systems for pre-listening the different channels or main signal on headphones.

This project is meant to be extended and played around with.
It should be easy to tweak the filters/eqs, change the midi mapping or
embed this in your own application.

%prep
%autosetup -n equis

%build

export RUSTFLAGS="-g -O"
export RUST_BACKTRACE=1

cargo build --release


%install 

install -m 755 -d %{buildroot}/%{_bindir}/

cp -ra target/release/equis-gui %{buildroot}/%{_bindir}/

%files
%doc README.md NOTES.md
%license LICENSE.md
%{_bindir}/*

%changelog
* Tue Sep 26 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
