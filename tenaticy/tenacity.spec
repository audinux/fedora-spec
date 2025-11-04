%global	optflags %{optflags} -fPIC

Summary: An easy-to-use multi-track audio editor and recorder
Name: tenacity
Version: 1.3.4
Release: 1%{?dist}
License: GPLv2+
Url: https://codeberg.org/tenacityteam/tenacity

# Usage: ./tenacity-sources.sh <TAG>
#        ./tenacity-source.sh v1.3.4

Source0: tenacity.tar.gz
Source1: tenacity-source.sh
Patch0:	tenacity-1.3.4-workaround-porttimer-library-not-found.patch
Patch1:	tenacity-1.3.4-fix-rpath.patch
Patch2:	tenacity-1.3.4-fix-missing-include.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: chrpath
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: git
BuildRequires: python
BuildRequires: yasm
BuildRequires: gettext-devel
BuildRequires: ladspa-devel
# Cmake explicitly searches for this
BuildRequires: wxGTK-devel
BuildRequires: alsa-lib-devel
BuildRequires: dbus-devel
BuildRequires: expat-devel
BuildRequires: flac-devel
BuildRequires: libglvnd-devel
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: jsoncpp-devel
BuildRequires: libid3tag-devel
BuildRequires: pkgconfig(jack)
BuildRequires: lame-devel
BuildRequires: (ffmpeg-devel or ffmpeg-free-devel)
BuildRequires: libmatroska-devel
BuildRequires: libzip-devel
BuildRequires: lilv-devel
BuildRequires: lv2-devel
BuildRequires: libmad-devel
BuildRequires: libogg-devel
BuildRequires: portaudio-devel
BuildRequires: portmidi-devel
BuildRequires: portsmf-devel
BuildRequires: rapidjson-devel
BuildRequires: serd-devel
BuildRequires: libsndfile-devel
BuildRequires: sord-devel
BuildRequires: soxr-devel
BuildRequires: soundtouch-devel
BuildRequires: sqlite-devel
BuildRequires: sratom-devel
BuildRequires: suil-devel
BuildRequires: taglib-devel
BuildRequires: twolame-devel
BuildRequires: vamp-plugin-sdk-devel
BuildRequires: libvorbis-devel
BuildRequires: zlib-ng-compat-devel

%description
This is an easy-to-use multi-track audio editor and recorder. It is not merely
an Audacity fork that removes error reporting and update checking,
although it might seem like it. We have been hard at work implementing our
own features and fixes and want to take Tenacity in a direction our users and
community like.
Features:
* Recording from audio devices (real or virtual).
* Export / Import a wide range of audio formats (extensible with FFmpeg).
* High quality including up to 32-bit float audio support.
* Plug-ins providing support for VST, LV2, and AU plugins.
* Scripting in the built-in scripting language Nyquist, or in Python, Perl and
  other languages with named pipes.
* Editing arbitrary sampling and multi-track timeline.
* Accessibility (editing via keyboard, screen reader and narration support).
* Tools useful in the analysis of signals, including audio.

%package libs
Summary: Libraries needed for %{name}
License: GPLv2+

%description libs
An easy-to-use multi-track audio editor and recorder.
This package contains the libraries needed by %{name}.

%prep
%autosetup -p1 -n tenacity

%build

%cmake 
%cmake_build

%install

%cmake_install

# Fix rpath
for File in %{buildroot}/%{_libdir}/tenacity/*.so
do
    chrpath --delete $File
done

for File in %{buildroot}/%{_libdir}/tenacity/modules/*.so
do
    chrpath --delete $File
done

# rename some files
mv %{buildroot}/%{_datadir}/pixmaps/gnome-mime-application-x-audacity-project.xpm %{buildroot}/%{_datadir}/pixmaps/gnome-mime-application-x-tenacity-project.xpm

# Fix desktop file
desktop-file-edit --set-key=Exec \
		  --set-value="tenacity %F" \
		  %{buildroot}%{_datadir}/applications/%{name}.desktop

# Fix icons placement: NNxNN/%%{name}.png --> NNxNN/apps/%%{name}.png
for N in 16 22 24 32 48;
do
    pushd %{buildroot}%{_iconsdir}/hicolor/${N}x${N}
    mkdir apps
    mv %{name}.png ./apps/
    popd
done

# Drop wrongly installed stuff from sources
rm -f %{buildroot}%{_datadir}/%{name}/help/*

# We take this with our macro
rm -f %{buildroot}%{_datadir}/doc/%{name}/LICENSE.txt

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/EQDefaultCurves.xml
%{_datadir}/%{name}/nyquist/rawwaves/*raw
%{_datadir}/%{name}/nyquist/*.lsp
%{_datadir}/%{name}/nyquist/*.txt
%{_datadir}/%{name}/plug-ins/*.ny
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/*.xpm
%{_mandir}/man1/%{name}.1*

%files libs
%{_libdir}/%{name}/lib-*.so
%{_libdir}/%{name}/modules/mod-*.so
%{_libdir}/libnyquist.so

%changelog
* Tue Nov 04 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.4-1
- initial spec from openmandriva
