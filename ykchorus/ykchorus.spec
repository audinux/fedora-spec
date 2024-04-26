# Tag: Jack, Alsa, Effect
# Type: Plugin, Standalone, LADSPA, VST, LV2, VST3, CLAP
# Category: Audio, Effect

Name: ykchorus
Version: 0.2.4
Release: 1%{?dist}
Summary: A chorus audio effect plugin based on DSP code by Togu Audio Line (TAL)
License: GPL-2.0-or-later
URL: https://github.com/SpotlightKid/ykchorus

Vendor:       Audinux
Distribution: Audinux

# ./ykchorus-source.sh <tag>
# ./ykchorus-source.sh v0.2.4

Source0: ykchorus.tar.gz
Source1: ykchorus-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: ladspa-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: desktop-file-utils

%description
A chorus effect inspired by the one found in certain well-known
Japanese vintage analog synthesizers (You Know which).

%package -n ladspa-%{name}
Summary: LADSPA version of the ykchorus plugin.

%package -n lv2-%{name}
Summary: LV2 version of the ykchorus plugin.

%package -n vst-%{name}
Summary: VST version of the ykchorus plugin.

%package -n vst3-%{name}
Summary: VST3 version of the ykchorus plugin.

%package -n clap-%{name}
Summary: CLAP version of the ykchorus plugin.

%description -n ladspa-%{name}
LADSPA version of the ykchorus plugin.

%description -n lv2-%{name}
LV2 version of the ykchorus plugin.

%description -n vst-%{name}
VST version of the ykchorus plugin.

%description -n vst3-%{name}
VST3 version of the ykchorus plugin.

%description -n clap-%{name}
CLAP version of the ykchorus plugin.

%prep
%autosetup -n %{name}

%ifarch x86_64
sed -i -e "s/\$(PREFIX)\/lib/\$(PREFIX)\/lib64/g" Makefile
%endif

%build

%set_build_flags

%make_build PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

%install

%make_install PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 ./resources/ykchorus.desktop %{buildroot}/%{_datadir}/applications/

install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
install -m 644 ./resources/ykchorus.png %{buildroot}/%{_datadir}/pixmaps/

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/ykchorus.desktop
%{_datadir}/pixmaps/ykchorus.png

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n ladspa-%{name}
%{_libdir}/ladspa/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Fri Apr 26 2024 Yann Collette <ycollette.nospam@free.fr> - 0.2.4-1
- update to 0.2.4-1

* Mon Mar 28 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.3-1
- Initial version of the spec file
