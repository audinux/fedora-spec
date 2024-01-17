Name:    stochas
Version: 1.3.9
Release: 4%{?dist}
Summary: A VST3 MIDI sequencer
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

# Use ./source-stochas.sh to get the sources (latest master for now)
# ./source-stochas.sh v1.3.9

URL:     https://github.com/surge-synthesizer/stochas
Source0: stochas.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: rsync
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: pkgconfig(jack)

%description
A VST3 MIDI sequencer

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}

sed -i -e "s/find_package/#find_package/g" cmake/versiontools.cmake

%build

%set_build_flags
%cmake -DCMAKE_CXX_FLAGS="-include utility $CXXFLAGS"

%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/Stochas.vst3/
%if 0%{?fedora} < 33
cp -r stochas_artefacts/VST3/Stochas.vst3/* %{buildroot}/%{_libdir}/vst3/Stochas.vst3/
%else
cp -r %{__cmake_builddir}/stochas_artefacts/VST3/Stochas.vst3/* %{buildroot}/%{_libdir}/vst3/Stochas.vst3/
%endif

install -m 755 -d %{buildroot}%{_bindir}/
%if 0%{?fedora} < 33
install -m 644 -p stochas_artefacts/Standalone/Stochas %{buildroot}/%{_bindir}/
%else
install -m 644 -p %{__cmake_builddir}/stochas_artefacts/Standalone/Stochas %{buildroot}/%{_bindir}/
%endif

%files
%doc README.md
%license COPYING
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Mon Dec 05 2022 Yann Collette <ycollette.nospam@free.fr> - 1.3.9-4
- update to 1.3.9-4

* Mon Nov 21 2022 Yann Collette <ycollette.nospam@free.fr> - 1.3.8-4
- update to 1.3.8-4

* Mon Oct 25 2021 Yann Collette <ycollette.nospam@free.fr> - 1.3.5-4
- update to 1.3.5-4 - update for Fedora 35

* Sun Jun 06 2021 Yann Collette <ycollette.nospam@free.fr> - 1.3.5-3
- update to 1.3.5-3

* Sun Dec 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.4-3
- update to 1.3.4-3 - fix install

* Mon Nov 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.4-2
- update to 1.3.4

* Sat Oct 3 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.3-2
- fix for fedora 33

* Sun Sep 6 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.3-1
- update to 1.3.3

* Thu Aug 13 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
