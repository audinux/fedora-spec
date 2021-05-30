# Tag: MIDI
# Type: Plugin, LV2
# Category: Audio, Synthesizer
# LastSourceUpdate: 2021

Summary: Old-school all-digital 4-oscillator subtractive polyphonic synthesizer with stereo fx.
Name:    padthv1
Version: 0.9.17
Release: 1%{?dist}
URL:     https://sourceforge.net/projects/%{name}
License: GPLv2+

Source0: https://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:  padthv1-0001-disable-strip.patch

Requires: hicolor-icon-theme

BuildRequires: gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: lv2-devel >= 1.2.0
BuildRequires: desktop-file-utils
BuildRequires: libsndfile-devel
BuildRequires: fftw-devel
BuildRequires: liblo-devel
BuildRequires: libappstream-glib

%description
Based on the PADsynth algorithm, by Paul Nasca (ZynAddSubFX), 
as a special variant of additive synthesis.

%package -n lv2-%{name}
Summary:  An LV2 port of synthv1
Requires: lv2
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n lv2-%{name}
An LV2 plugin of the padthv1 synthesizer

%prep
%autosetup -p1

# Remove cruft from appdata file
pushd src/appdata
iconv -f utf-8 -t ascii//IGNORE -o tmpfile %{name}.appdata.xml 2>/dev/null || :
mv -f tmpfile %{name}.appdata.xml
popd

%build

%configure
%make_build

%install

%make_install
chmod +x %{buildroot}%{_libdir}/lv2/%{name}.lv2/%{name}.so
install -m 0644 src/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%doc AUTHORS README
%license COPYING
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_bindir}/%{name}_jack
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/man/man1/%{name}*
%{_datadir}/metainfo/%{name}.appdata.xml

%files -n lv2-%{name}
%{_libdir}/lv2/%{name}.lv2/

%changelog
* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.17-1
- update to 0.9.17-1 + fix debug build

* Fri Mar 27 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.13-1
- update to 0.9.13-1

* Sun Mar 15 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.12-1
- Initial spec file
