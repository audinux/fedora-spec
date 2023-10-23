# Tag: Jack, Emulator
# Type: Standalone, LV2
# Category: Audio, Programming
# GUIToolkit: Gtk2
# LastSourceUpdate: 2018

Name:    foo-yc20
Version: 1.3.0
Release: 2%{?dist}
Summary: A Faust emulation on a Yamaha YC20 Combo organ
License: MIT
URL:     https://github.com/sampov2/foo-yc20

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/sampov2/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cairo-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: gtk2-devel
BuildRequires: lv2-devel
BuildRequires: desktop-file-utils

%description
This is a Faust implementation of a 1969 designed Yamaha combo organ, the YC-20.
In addition to the Faust code, it has a Gtkmm UI with Jack audio and midi support.
A LV2 instrument plugin is planned but not yet executed.

%prep

%autosetup

%build
%make_build

%install

install -Dm 755 foo-yc20     %{buildroot}/%{_bindir}/foo-yc20
install -Dm 755 foo-yc20-cli %{buildroot}/%{_bindir}/foo-yc20-cli

install -d %{buildroot}/%{_datadir}/foo-yc20/graphics
install -m 644 graphics/*.png %{buildroot}/%{_datadir}/foo-yc20/graphics

cat foo-yc20.desktop.in | sed 's:%PREFIX%:{_datadir}:' > foo-yc20.desktop
install -Dm 644 foo-yc20.desktop %{buildroot}/%{_datadir}/applications/foo-yc20.desktop
rm foo-yc20.desktop

install -d %{buildroot}/%{_libdir}/lv2/foo-yc20.lv2
install -m 755 src/foo-yc20.lv2/*.so  %{buildroot}/%{_libdir}/lv2/foo-yc20.lv2
install -m 644 src/foo-yc20.lv2/*.ttl %{buildroot}/%{_libdir}/lv2/foo-yc20.lv2

desktop-file-install --vendor '' \
        --add-category="Audio;AudioVideo;" \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/foo-yc20.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/foo-yc20.desktop

%files
%license LICENSE
%doc README
%{_bindir}/foo-yc20
%{_bindir}/foo-yc20-cli
%{_libdir}/lv2/foo-yc20.lv2
%{_datadir}/applications/foo-yc20.desktop
%{_datadir}/foo-yc20

%changelog
* Tue May 5 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-2
- update for Fedora 32

* Wed Oct 31 2018 L.L.Robinson <baggypants@fedoraproject.org> - 1.3.0-2
- updated buildrequires for copr/koji

* Mon Oct 15 2018 L.L.Robinson <baggypants@fedoraproject.org>
- initial version of the spec file
