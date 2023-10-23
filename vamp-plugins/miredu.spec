# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: miredu
Version: 1.0
Release: 2%{?dist}
Summary: A Vamp plugin implementing basic audio descriptors for educational purposes
License: GLPv2
URL: https://github.com/MTG/miredu

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/MTG/miredu/archive/refs/heads/master.zip#/%{name}-master.zip

BuildRequires: gcc gcc-c++ make
BuildRequires: vamp-plugin-sdk-devel

%description
MIR.EDU is an open source vamp plug-in library written in C++ which implements
a basic set of descriptors useful for teaching MIR. The idea is to provide a
simple library with clear and well documented code for learning about audio
descriptors (RMS, log attack-time, spectral flux, etc.).

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
MIR.EDU is an open source vamp plug-in library written in C++ which implements
a basic set of descriptors useful for teaching MIR. The idea is to provide a
simple library with clear and well documented code for learning about audio
descriptors (RMS, log attack-time, spectral flux, etc.).

%prep
%autosetup -n %{name}-master

sed -i -e "s/\$(VAMP_SDK_DIR)\/libvamp-sdk.a/-lvamp-sdk/g" Makefile.linux
sed -i -e "s/CXXFLAGS := /CXXFLAGS := \$(CXXFLAGS) /g" Makefile.linux

%build

%set_build_flags

%make_build -f Makefile.linux

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 mir-edu.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 mir-edu.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 mir-edu.n3  %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%license LICENSE.txt
%doc README.md
%{_libdir}/vamp/mir-edu.*

%changelog
* Fri Jul 22 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-2
- update to 1.0-2

* Wed Jan 12 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial spec file

