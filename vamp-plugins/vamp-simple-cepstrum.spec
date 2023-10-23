# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: vamp-simple-cepstrum
Version: 1.0
Release: 2%{?dist}
Summary: A simple Vamp plugin to calculate and return cepstrum values from DFT bins
License: GLPv2
URL: https://code.soundsoftware.ac.uk/projects/vamp-simple-cepstrum

Vendor:       Audinux
Distribution: Audinux

Source0: https://code.soundsoftware.ac.uk/hg/vamp-simple-cepstrum/archive/tip.zip#/%{name}.zip

BuildRequires: gcc gcc-c++ make
BuildRequires: vamp-plugin-sdk-devel

%description
A simple Vamp plugin to calculate and return cepstrum values from DFT bins.
Useful as a preliminary tool for looking at cepstral data for simple pitch
or envelope methods.

%prep
%autosetup -n %{name}-a17bca16933a

sed -i -e "s/-Wall -g -fPIC/\$(VAMPCFLAGS)/g" Makefile.linux64
sed -i -e "s/-Wl,-Bstatic //g" Makefile.linux64

%build

%set_build_flags

export VAMPCFLAGS="$CFLAGS -fPIC"

%make_build -f Makefile.linux64

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 simple-cepstrum.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 simple-cepstrum.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 simple-cepstrum.n3  %{buildroot}/%{_libdir}/vamp/

%files
%license COPYING
%doc README
%{_libdir}/vamp/simple-cepstrum.*

%changelog
* Fri Jul 22 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1-2
- update to 1.1-2

* Sat Jan 08 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1-1
- Initial spec file

