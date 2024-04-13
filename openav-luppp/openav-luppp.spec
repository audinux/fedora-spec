# Tag: Jack, Loop
# Type: Standalone
# Category: Audio, Sequencer

%global realname openAV-Luppp

Name: openav-luppp
Version: 1.1
Release: 11%{?dist}
Summary: Live performance mixing tool
License: GPLv3
URL: http://openavproductions.com/luppp

Source0: https://github.com/harryhaaren/openAV-Luppp/archive/release-%{version}.tar.gz
Source1: loop.svg
Source2: luppp.desktop
Source3: luppp.appdata.xml

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: non-ntk-devel
BuildRequires: chrpath
BuildRequires: libappstream-glib
BuildRequires: appdata-tools
BuildRequires: desktop-file-utils

Requires: hicolor-icon-theme

%description
Luppp is a music creation tool, intended for live use. It focuses on
real time processing and a fast intuitive workflow. It uses Jack
for audio output.

%prep
%autosetup -n %{realname}-release-%{version}

sed -i 's|SET(CMAKE_CXX_FLAGS ".*")|SET(CMAKE_CXX_FLAGS "%{optflags}")|;
        s|SET(CMAKE_C_FLAGS ".*")|SET(CMAKE_C_FLAGS "%{optflags}")|;
        s|-msse2||' src/CMakeLists.txt

%build

echo '#define GIT_VERSION "%{version}-%{release}"' > src/version.hxx
%cmake -DRELEASE_BUILD=1
%cmake_build

%install

install -p -D %{__cmake_builddir}/src/luppp %{buildroot}%{_bindir}/luppp
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -av resources/controllers %{buildroot}%{_datadir}/%{name}/
cp -av src/resources/luppp.prfs %{buildroot}%{_datadir}/%{name}/
install -p -Dm0644 %SOURCE1 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/luppp.svg
install -p -Dm0644 %SOURCE3 %{buildroot}%{_datadir}/appdata/luppp.appdata.xml

desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE2}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/luppp.appdata.xml

chrpath --delete %{buildroot}/%{_bindir}/luppp

%files
%{_bindir}/luppp
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/*.appdata.xml
%doc LICENSE CHANGELOG README.md

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-4
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1-1
- Update to latest release (bugfixes, minor features)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May  4 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.1-1
- New upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0-3
- Install .desktop file properly and extend %%post/%%postun
- Update Requires and BuildRequires
- Preserve timestamps

* Mon Feb 10 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0-2
- Tweak .desktop file

* Fri Dec 13 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0-1
- Initial package
