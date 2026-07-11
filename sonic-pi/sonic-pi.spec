# Status: inactive
# Tag: Editor, Live
# Type: Standalone, Language
# Category: Audio, Programming
# GUIToolkit: Qt6

# Have a look at:
# https://github.com/archlinux/svntogit-community/tree/packages/sonic-pi/trunk

# Do not check any files here for requires
%global __requires_exclude_from (^.*/vendor/.*$|^.*/native/.*$)

%global __mangle_shebangs_exclude_from /vendor/
%global __mangle_shebangs_exclude ruby

%global _smp_build_ncpus 1
%global debug_package %{nil}

Name: sonic-pi
Version: 4.6.0
Release: 13%{?dist}
Summary: A musical programming environment
License: MIT
URL: https://sonic-pi.net/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/sonic-pi-net/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: sonic-pi-0001-fix-system-paths.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: vcpkg
BuildRequires: elixir
BuildRequires: patchelf
BuildRequires: qt6-linguist
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel
BuildRequires: qt6-qtsvg-devel
BuildRequires: supercollider-devel
BuildRequires: libffi-devel
BuildRequires: ruby-devel
BuildRequires: aubio-devel
BuildRequires: boost-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: rtmidi-devel
BuildRequires: fmt-devel
BuildRequires: aubio-devel
BuildRequires: glew-devel
BuildRequires: erlang-erts
BuildRequires: ruby
BuildRequires: rubygem-rake
BuildRequires: rubygem-bundler
BuildRequires: rubygem-racc
%if 0%{?fedora} >= 34
BuildRequires: rubygem-rexml
%endif
BuildRequires: zlib-devel
BuildRequires: libuuid-devel
BuildRequires: reproc-devel
BuildRequires: SDL2-devel
BuildRequires: libsndfile-devel
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel
BuildRequires: libpng-devel
BuildRequires: libatomic
BuildRequires: desktop-file-utils

Requires(pre): pulseaudio-module-jack
Requires(pre): supercollider-sc3-plugins
Requires(pre): supercollider
Requires(pre): ruby
Requires(pre): rubygem-racc
Requires(pre): aubio
Requires(pre): osmid
Requires(pre): libatomic

%description
Sonic Pi is an open source programming environment designed to explore and
teach programming concepts through the process of creating new sounds.
Comes with an associated scheme of work which emphasizes the importance of
creativity in the learning process and gives users the control to turn their
sonic ideas into reality.

%prep
%autosetup -p1 -n %{name}-%{version}

# From logs:
# /usr/bin/ruby-mri: No such file or directory -- /app/server/ruby/bin/clear-logs.rb (LoadError)
# /usr/bin/ruby-mri: No such file or directory -- /app/server/ruby/bin/daemon.rb (LoadError)
# [GUI] - could not open file /usr/bin/../../../app/gui/theme/light/doc-styles.css
# [GUI] - could not open file /usr/bin/../../../app/gui/theme/app.qss

# app/api/src/sonicpi_api.cpp
#    m_paths[SonicPiPath::FetchUrlPath]        = m_paths[SonicPiPath::RootPath] / "app/server/ruby/bin/fetch-url.rb";
#    m_paths[SonicPiPath::ClearLogsPath]        = m_paths[SonicPiPath::RootPath] / "app/server/ruby/bin/clear-logs.rb";

# app/linux-build-gui.sh:cmake --build .
# app/linux-config.sh:cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE="$config" ..

# remove make clean
sed -i -e "/make clean/d" app/server/ruby/bin/compile-extensions.rb
sed -i -e "s/erl -make//g" app/linux-prebuild.sh

# remove some compiled ruby package
sed -i -e "/interception/d" app/server/ruby/bin/compile-extensions.rb

# remove aubio for prebuild
sed -i -e "/aubio/d" app/linux-prebuild.sh

# remove osx rubygem
rm -rf app/server/ruby/vendor/narray-0.6.1.1/
rm -rf app/server/ruby/vendor/ruby-coreaudio-0.0.12-patched/

# remove unused rubygem
rm -rf app/server/ruby/vendor/interception/
rm -rf app/server/ruby/vendor/ast-2.0.0/
rm -rf app/server/ruby/vendor/blankstate/
rm -rf app/server/ruby/vendor/benchmark-ips-2.3.0
rm -rf app/server/ruby/vendor/metaclass-0.0.4
rm -rf app/server/ruby/vendor/mocha-1.1.0
rm -rf app/server/ruby/vendor/rake-compiler-1.1.0
rm -rf app/server/ruby/vendor/rouge

# install some gems
gem install prime -v 0.1.2

%build

cd app

%set_build_flags

./linux-build-all.sh

%install

mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/%{name}/app/gui/theme/
mkdir -p %{buildroot}%{_datadir}/%{name}/etc/
mkdir -p %{buildroot}%{_datadir}/applications/
cp -ra app/gui/theme/*    %{buildroot}%{_datadir}/%{name}/app/gui/theme/
cp app/build/gui/sonic-pi %{buildroot}%{_bindir}/%{name}
cp -ra etc/*              %{buildroot}%{_datadir}/%{name}/etc/

mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp app/gui/images/icon-smaller.png %{buildroot}%{_datadir}/pixmaps/

mkdir -p %{buildroot}%{_datadir}/%{name}/app/server/native/osmid/
ln -s /usr/bin/m2o %{buildroot}%{_datadir}/%{name}/app/server/native/osmid/
ln -s /usr/bin/o2m %{buildroot}%{_datadir}/%{name}/app/server/native/osmid/

mkdir -p %{buildroot}%{_datadir}/%{name}/app/server/ruby/bin/
cp -ra  app/server/ruby/bin/* %{buildroot}%{_datadir}/%{name}/app/server/ruby/bin/

# Manage ruby version for various Fedora version
%define rb_version "2.4.0"
%if 0%{?fedora} >= 28
%define rb_version "2.5.0"
%endif
%if 0%{?fedora} >= 30
%define rb_version "2.6.0"
%endif
%if 0%{?fedora} >= 32
%define rb_version "2.7.0"
%endif
%if 0%{?fedora} >= 34
%define rb_version "3.0.0"
%endif
%if 0%{?fedora} >= 36
%define rb_version "3.1.0"
%endif
%if 0%{?fedora} >= 41
%define rb_version "3.3.0"
%endif
%if 0%{?fedora} >= 42
%define rb_version "3.4.0"
%endif
%if 0%{?fedora} >= 44
%define rb_version "4.0.0"
%endif

mkdir -p %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/%{rb_version}/

cp -ra app/server/ruby/rb-native/%{rb_version}/* %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/%{rb_version}/
cp -ra app/server/ruby/*.rb %{buildroot}%{_datadir}/%{name}/app/server/ruby/

mkdir -p %{buildroot}%{_datadir}/%{name}/app/server/ruby/vendor/
cp -ra app/server/ruby/vendor/* %{buildroot}%{_datadir}/%{name}/app/server/ruby/vendor/

mkdir -p %{buildroot}%{_datadir}/%{name}/app/server/ruby/lib/
cp -ra app/server/ruby/lib/* %{buildroot}%{_datadir}/%{name}/app/server/ruby/lib/

mkdir -p %{buildroot}%{_datadir}/%{name}/app/server/beam/
cp -ra app/server/beam/tau %{buildroot}%{_datadir}/%{name}/app/server/beam/

rm %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/%{rb_version}/rugged/rugged.so
ln -s %{_datadir}/%{name}/app/server/ruby/vendor/rugged-1.9.0/ext/rugged/rugged.so \
   %{buildroot}%{_datadir}/%{name}/app/server/ruby/rb-native/%{rb_version}/rugged/rugged.so

find %{buildroot}%{_datadir}/%{name}/etc/wavetables/ -name "AdventureKidWaveforms.txt" -exec chmod a-x {} \;

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%name
Exec=%{name}
Icon=icon-smaller
Comment=Music live coding for everyone
Comment[es]=Programación de música en vivo al alcance de cualquiera
Terminal=false
Type=Application
Categories=AudioVideo;Audio;
X-AppInstall-Package=%{name}
EOF

# Remove build artifacts from the vendor gem tree.
# Parentheses are mandatory: without them find's operator precedence makes
# -delete (or -exec) bind only to the last -name condition, leaving all other
# patterns matched but not acted on.
find %{buildroot}/%{_datadir}/%{name}/app/server/ruby/vendor -type f \
    \( -name "*.o"    -o -name "*.c"    -o -name "*.h"    \
    -o -name "*.a"    -o -name "*.txt"  -o -name "*.md"   \
    -o -name "*.html" -o -name "*.text" -o -name "*.log"  \
    -o -name "extconf.rb" -o -name "Makefile" -o -name "*.mk" \
    -o -name "*.gemspec"  -o -name "Rakefile"              \) \
    -delete 2>/dev/null || true

# Remove test / spec / benchmark directories from vendor gems
find %{buildroot}/%{_datadir}/%{name}/app/server/ruby/vendor -depth -type d \
    \( -name "test" -o -name "spec" -o -name "tests" -o -name "benchmark" \) \
    -exec rm -rf {} + 2>/dev/null || true

# Install KissFFT
install -m 755 -d %{buildroot}/%{_libdir}/sonic-pi/
cp app/build/kissfft-*/libkissfft-float.so.* %{buildroot}/%{_libdir}/sonic-pi/

# Fix rpath problem
patchelf --set-rpath '$ORIGIN/../%{_lib}/sonic-pi/' %{buildroot}/%{_bindir}/sonic-pi

# Fix some python interp
sed -i -e "s|env python|env python3|g" %{buildroot}/%{_datadir}/sonic-pi/app/server/ruby/vendor/rugged-1.9.0/vendor/libgit2/script/release.py

# Install desktop file
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc CHANGELOG.md COMMUNITY.md CONTRIBUTING.md CONTRIBUTORS.md FAQ.md README.md SYNTH_DESIGN.md TYPES-OF-CONTRIBUTIONS.md
%license LICENSE.md
%{_bindir}/sonic-pi
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%dir %{_datadir}/sonic-pi
%{_datadir}/sonic-pi/*
%{_libdir}/sonic-pi/*.so*

%changelog
* Fri Jul 10 2026 Yann Collette <ycollette.nospam@free.fr> 4.6.0-13
- fix vendor cleanup find command: missing parentheses around -o conditions
  caused -delete/-exec to bind only to the last pattern (*.md), leaving all
  other build artifacts (*.o *.c *.h *.a Makefile extconf.rb etc.) unremoved
- add missing patterns to cleanup: extconf.rb Makefile *.mk *.gemspec Rakefile *.log
- add separate find pass to remove test/ spec/ benchmark/ dirs from vendor gems
- switch to -type f -delete (faster and safer than -exec rm -rf {})

* Fri Jul 10 2026 Yann Collette <ycollette.nospam@free.fr> 4.6.0-12
- fix rugged symlink: 0.28.4.1 → 1.9.0 (version shipped in 4.6.0 vendor tree)
- remove erroneous rm -rf rugged-1.9.0/ that broke the symlink target
- fix Source0 URL: samaaron/sonic-pi → sonic-pi-net/sonic-pi (upstream moved)
- drop BuildRequires crossguid2-devel, gsl-lite-devel (not used by 4.6.0 cmake)
- fix rb_version for Fedora 41+: 4.0.0 → 3.3.0 (Ruby 4.0 does not exist)
- fix GUIToolkit comment: Qt5 → Qt6

* Sun Jul 05 2026 Yann Collette <ycollette.nospam@free.fr> 4.6.0-11
- update to 4.6.0-11

* Thu Sep 15 2022 Yann Collette <ycollette.nospam@free.fr> 4.2.0-11
- update to 4.2.0-11

* Tue Aug 30 2022 Yann Collette <ycollette.nospam@free.fr> 4.1.0-11
- update to 4.1.0-11

* Sun Jul 17 2022 Yann Collette <ycollette.nospam@free.fr> 4.0.3-11
- update to 4.0.3-11

* Wed Jul 13 2022 Yann Collette <ycollette.nospam@free.fr> 4.0.1-11
- update to 4.0.1-11

* Thu Jul 07 2022 Yann Collette <ycollette.nospam@free.fr> 4.0.0-11
- update to 4.0.0-11

* Thu Apr 14 2022 Yann Collette <ycollette.nospam@free.fr> 3.3.1-11
- update to 3.3.1-11 - fixed for Fedora 36

* Mon Mar 29 2021 Yann Collette <ycollette.nospam@free.fr> 3.3.1-10
- update to 3.3.1-10 - fixed for Fedora 34

* Mon Feb 1 2021 Yann Collette <ycollette.nospam@free.fr> 3.3.1-7
- update to 3.3.1-7

* Fri Jan 29 2021 Yann Collette <ycollette.nospam@free.fr> 3.3.0-7
- update to 3.3.0-7 - do some cleanup

* Thu Jan 28 2021 Yann Collette <ycollette.nospam@free.fr> 3.3.0-6
- update to 3.3.0-6

* Fri Apr 24 2020 Yann Collette <ycollette.nospam@free.fr> 3.2.2-6
- fix for Fedora a32

* Mon Apr 6 2020 Yann Collette <ycollette.nospam@free.fr> 3.2.2-5
- update to 3.2.2-5

* Sun Mar 22 2020 Yann Collette <ycollette.nospam@free.fr> 3.2.0-5
- fix spec file - update oscmid to v0.6.8

* Mon Mar 2 2020 Yann Collette <ycollette.nospam@free.fr> 3.2.0-4
- update to 3.2.0-4

* Sun Mar 1 2020 Yann Collette <ycollette.nospam@free.fr> 3.2.0-3
- update to 3.2.0

* Thu Nov 7 2019 Yann Collette <ycollette.nospam@free.fr> 3.1.0-3
- fix for Fedora 31

* Thu May 2 2019 Yann Collette <ycollette.nospam@free.fr> 3.1.0-3
- update for Fedora 30

* Tue Mar 26 2019 Yann Collette <ycollette.nospam@free.fr> 3.1.0-3
- update to master (and add rugged-0.28.0)

* Fri Dec 7 2018 Yann Collette <ycollette.nospam@free.fr> 3.1.0-3
- fix for Fedora 29 - update to master (to get rugged-0.27.5)

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> 3.1.0-2
- update for Fedora 29

* Tue Apr 17 2018 Yann Collette <ycollette.nospam@free.fr> update build process
- update build process
- update to 3.1.0
- remove duplicated so

* Thu Oct 26 2017 Yann Collette <ycollette.nospam@free.fr> update to 3.0.1
- update to 3.0.1

* Mon Dec 28 2015 Ismael Olea <ismael@olea.org> 2.8.0-2
- Added missed supercollider-sc3-plugins dependency https://github.com/samaaron/sonic-pi/issues/897#issuecomment-167682120

* Mon Dec 28 2015 Ismael Olea <ismael@olea.org> 2.8.0-1
- updating to 2.8.0

* Fri Dec 13 2013 Amadeus Konopko a.konopko@hotmail.com 0-0.3
- Added armv6 architecture build, removed some requires.

* Fri Dec 6 2013 Amadeus Konopko a.konopko@hotmail.com 0-0.2
- Modified files list to only include app folder, README, and LICENSE.

* Fri Nov 22 2013 Amadeus Konopko a.konopko@hotmail.com 0-0.1
- Made an initial rpm to package the sonic-pi application.

