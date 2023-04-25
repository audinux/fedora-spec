Name:    aida-x
Version: 1.0.0
Release: 1%{?dist}
Summary: An Amp Model Player leveraging AI
License: GPLv2+
URL:     https://github.com/AidaDSP/AIDA-X

Vendor:       Audinux
Distribution: Audinux

# To get aidax source code:
# $ ./aidax-source.sh 1.0.0

Source0: AIDA-X.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: SDL2-devel
BuildRequires: dbus-devel

%description
AIDA-X is an Amp Model Player, allowing it to load models
of AI trained music gear, which you can then play through! guitar

Its main intended use is to provide high fidelity simulations of amplifiers.
However, it is also possible to run entire signal chains consisting of
any combination of amp, cab, dist, drive, fuzz, boost and eq.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst-%{name}
VST2 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n AIDA-X

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 -d %{buildroot}%{_libdir}/clap/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/

cp -ra %{__cmake_builddir}/bin/AIDA-X %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/bin/AIDA-X.clap %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/bin/AIDA-X.lv2 %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/bin/AIDA-X-vst2.so %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/bin/AIDA-X.vst3 %{buildroot}%{_libdir}/vst3/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Tue Apr 25 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- update to 1.0.0-1

* Sat Apr 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- update to 0.2.0-1

* Wed Apr 05 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial build
