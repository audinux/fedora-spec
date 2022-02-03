# Tag: Jack, Alsa, MIDI
# Type: Standalone
# Category: Audio, Sequencer

# Version: d958df0486c7397c243f5ac36bf4acbc461a1e50

Name:    non-daw-lv2
Version: 1.2.0
Release: 11.gitd958df04%{?dist}
Summary: A digital audio workstation for JACK with LV2 plugins
License: GPLv2+
URL:     https://github.com/falkTX/non

Vendor:       Audinux
Distribution: Audinux

Source0: non-daw-lv2.tar.gz
Source1: non-daw-lv2-sources.sh

# To get the source package:
# ./non-daw-lv2-sources.sh

BuildRequires: gcc gcc-c++ make
BuildRequires: non-ntk-devel
BuildRequires: non-ntk-fluid
BuildRequires: liblo-devel
BuildRequires: libsndfile-devel
BuildRequires: fltk-fluid
BuildRequires: fltk-devel
BuildRequires: libsigc++20-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libXpm-devel
BuildRequires: ladspa-devel
BuildRequires: liblrdf-devel
BuildRequires: lilv-devel
BuildRequires: lv2-devel
BuildRequires: python-unversioned-command
BuildRequires: desktop-file-utils

%description
Non-daw-lv2 is a digital audio workstation for JACK.
It suppors LV2 plugins.

%package -n non-mixer-lv2
Summary:  A digital audio mixer for JACK
Requires: non-daw

%description -n non-mixer-lv2
non-mixer is a powerful, reliable and fast modular Digital Audio Mixer

%prep
%autosetup -n non-daw-lv2

sed -i -e "s/#define USER_CONFIG_DIR \".non-mixer\/\"/#define USER_CONFIG_DIR \".non-mixer-lv2\/\"/g" mixer/src/main.C
sed -i -e "s/if ( ! strcmp( n, \"non-mixer-noui\" ) )/if ( ! strcmp( n, \"non-mixer-noui\" ) )/g"     mixer/src/main.C
sed -i -e "s/DOCUMENT_PATH \"\/non-mixer\/MANUAL\"/DOCUMENT_PATH \"\/non-mixer-lv2\/MANUAL\"/g"       mixer/src/Mixer.C

sed -i -e "/MIDI\/midievent.C/{x;//!d;x}" nonlib/wscript

%build
CFLAGS="%{optflags}" CXXFLAGS="%{optflags} -std=c++11" ./waf configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-debug
./waf %{?_smp_mflags} -v 

%install 
./waf install --destdir=%{buildroot} --docdir=%{buildroot}/%{_docdir}/

mv %{buildroot}/%{_bindir}/non-mixer                       %{buildroot}/%{_bindir}/non-mixer-lv2
mv %{buildroot}/%{_bindir}/non-midi-mapper                 %{buildroot}/%{_bindir}/non-midi-mapper-lv2
mv %{buildroot}/%{_datadir}/applications/non-mixer.desktop %{buildroot}/%{_datadir}/applications/non-mixer-lv2.desktop
mv %{buildroot}/%{_datadir}/pixmaps/non-mixer              %{buildroot}/%{_datadir}/pixmaps/non-mixer-lv2
mv %{buildroot}/%{_datadir}/doc/non-mixer                  %{buildroot}/%{_datadir}/doc/non-mixer-lv2

rm %{buildroot}/%{_bindir}/non-mixer-noui
CWD=`pwd`
cd %{buildroot}/%{_bindir}/
ln -s non-mixer-lv2 non-mixer-noui-lv2
cd $CWD

Resolution="128x128 16x16 192x192 256x256 32x32 36x36 48x48 512x512 64x64 72x72 96x96"
for Dirs in $Resolution
do
  rm %{buildroot}/%{_datadir}/icons/hicolor/$Dirs/apps/non-mixer.png
  rm %{buildroot}/%{_datadir}/icons/hicolor/$Dirs/apps/non-sequencer.png
  rm %{buildroot}/%{_datadir}/icons/hicolor/$Dirs/apps/non-session-manager.png
  rm %{buildroot}/%{_datadir}/icons/hicolor/$Dirs/apps/non-timeline.png
done

sed -i -e "s/non-mixer/non-mixer-lv2/g" %{buildroot}/%{_datadir}/applications/non-mixer-lv2.desktop

# correct permissions
chmod 755 %{buildroot}%{_bindir}/non-mixer*

# cleanup
rm -f %{buildroot}/%{_prefix}/bin/bin/import-ardour-session
rm -f %{buildroot}/%{_prefix}/bin/import-ardour-session_gui
rm -f %{buildroot}/%{_prefix}/bin/jackpatch
rm -f %{buildroot}/%{_prefix}/bin/non-daw
rm -f %{buildroot}/%{_prefix}/bin/non-sequencer
rm -f %{buildroot}/%{_prefix}/bin/non-session-manager
rm -f %{buildroot}/%{_prefix}/bin/non-timeline
rm -f %{buildroot}/%{_prefix}/bin/nsm-proxy
rm -f %{buildroot}/%{_prefix}/bin/nsm-proxy-gui
rm -f %{buildroot}/%{_prefix}/bin/nsmd

rm -f %{buildroot}/%{_prefix}/lib/debug/usr/bin/import-ardour-session_gui-%{version}-%{release}.%{dist}.debug
rm -f %{buildroot}/%{_prefix}/lib/debug/usr/bin/jackpatch-%{version}-%{release}.%{dist}.debug
rm -f %{buildroot}/%{_prefix}/lib/debug/usr/bin/non-sequencer-%{version}-%{release}.%{dist}.debug
rm -f %{buildroot}/%{_prefix}/lib/debug/usr/bin/non-session-manager-%{version}-%{release}.%{dist}.debug
rm -f %{buildroot}/%{_prefix}/lib/debug/usr/bin/non-timeline-%{version}-%{release}.%{dist}.debug
rm -f %{buildroot}/%{_prefix}/lib/debug/usr/bin/nsm-proxy-%{version}-%{release}.%{dist}.debug
rm -f %{buildroot}/%{_prefix}/lib/debug/usr/bin/nsm-proxy-gui-%{version}-%{release}.%{dist}.debug
rm -f %{buildroot}/%{_prefix}/lib/debug/usr/bin/nsmd-%{version}-%{release}.%{dist}.debug

rm %{buildroot}/%{_prefix}/share/applications/non-sequencer.desktop
rm %{buildroot}/%{_prefix}/share/applications/non-session-manager.desktop
rm %{buildroot}/%{_prefix}/share/applications/non-timeline.desktop

rm -rf %{buildroot}/%{_prefix}/share/doc/non-sequencer/
rm -rf %{buildroot}/%{_prefix}/share/doc/non-session-manager/
rm -rf %{buildroot}/%{_prefix}/share/doc/non-timeline/
rm -rf %{buildroot}/%{_prefix}/share/non-sequencer
rm %{buildroot}/%{_prefix}/share/pixmaps/non-sequencer/icon-256x256.png
rm %{buildroot}/%{_prefix}/share/pixmaps/non-session-manager/icon-256x256.png
rm %{buildroot}/%{_prefix}/share/pixmaps/non-timeline/icon-256x256.png

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/non-mixer-lv2.desktop

%files -n non-mixer-lv2
%license COPYING
%{_bindir}/non-mixer-lv2
%{_bindir}/non-mixer-noui-lv2
%{_bindir}/non-midi-mapper-lv2
%{_docdir}/non-mixer-lv2
%{_datadir}/applications/non-mixer-lv2.desktop
%{_datadir}/pixmaps/non-mixer-lv2

%changelog
* Wed Jan 05 2022 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-11.gitd958df04
- update desktop

* Thu Mar 19 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-10.gitd958df04
- initial spec file
