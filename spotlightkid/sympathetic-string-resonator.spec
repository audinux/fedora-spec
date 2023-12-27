Name:    sympathetic-string-resonator
Version: 0.1
Release: 1%{?dist}
Summary: A sympathetic string resonator
License: MIT
URL:     https://github.com/SpotlightKid/sympathetic-string-resonator

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./spotlightkid-source.sh <project> <tag>
# ./spotlightkid-source.sh sympathetic-string-resonator a6c5a110c9c1d69505ee6f524c46f903a0920b6e

Source0: sympathetic-string-resonator.tar.gz
Source1: spotlightkid-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: ladspa-devel

%description
A sympathetic string resonator

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  MIT
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n %{name}

%ifarch aarch64
sed -i -e "/AVX.cpp/d" libs/strings/Makefile
sed -i -e "/SSE.cpp/d" libs/strings/Makefile
%endif

%build

%set_build_flags

%ifarch x86_64
%make_build SKIP_STRIPPING=true
%else
%make_build SKIP_STRIPPING=true CPU_I386_OR_X86_64=0
%endif

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_bindir}/

cd bin
cp -a ssr %{buildroot}/%{_bindir}/
cp -ra ssr.lv2 %{buildroot}/%{_libdir}/lv2/
cd ..

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Wed Dec 27 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
