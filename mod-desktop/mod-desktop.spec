# Status: active
# Tag: Rack, Jack, Qt
# Type: Standalone
# Category: Audio, Effect

# mod-desktop itself (fork of mod-audio/mod-desktop, 'fedora' branch): adds
# the SYSTEM_DEPS=1 Linux build mode (native compiler, system Qt5/JACK/LV2
# libraries and system Python packages, no PawPaw) and connects to an
# already-running JACK or PipeWire-JACK server instead of bundling/starting
# its own jackd, matching how Fedora normally runs audio (pipewire-jack).
%global commit0 97175358035d5e96332b44e95ed62d23a4fdf08e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# mod-ui (fork of mod-audio/mod-ui, 'fedora' branch), bundled as src/mod-ui:
# the release-pinned mod-ui submodule only supports Tornado 4, while Fedora
# ships Tornado 6; this fork carries the corrected coroutine and
# stream-callback compatibility code the SYSTEM_DEPS build requires.
%global mod_ui_commit 93e1a04f107d0290fe457d886bff5c57cf1d465c

# mod-host and mod-midi-merger (upstream mod-audio, unmodified): bundled as
# src/mod-host and src/mod-midi-merger at the commits mod-desktop's own
# submodule pins reference, built from source as private, non-PATH helper
# binaries (see below) rather than taken from the separate mod-host package.
%global mod_host_commit 754070f94bffafb51c7f3d86df47bc04b00f1151
%global mod_midi_merger_commit db24bd754ff01134e5eca0fb7a5ec188eab2e329

Name: mod-desktop
Version: 0.0.13.%{shortcommit0}
Release: 1%{?dist}
License: AGPL-3.0-or-later AND GPL-3.0-or-later AND ISC
Summary: System-tray launcher for the MOD pedalboard UI, using system JACK/PipeWire
URL: https://github.com/mod-audio/mod-desktop
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Source tarball assembled offline by mod-desktop-source.sh from:
#   https://github.com/ycollet/mod-desktop       branch fedora, commit %{commit0}
#   https://github.com/ycollet/mod-ui            branch fedora, commit %{mod_ui_commit}
#   https://github.com/mod-audio/mod-host        commit %{mod_host_commit}
#   https://github.com/mod-audio/mod-midi-merger commit %{mod_midi_merger_commit}
# Run ./mod-desktop-source.sh to (re)produce %{name}-%{shortcommit0}.tar.gz
Source0: %{name}-%{shortcommit0}.tar.gz
Source1: mod-desktop-source.sh

# mod-host's Makefile infers jack_max_cpu_load() availability purely from
# jack.pc's reported version, but Fedora's default JACK provider,
# pipewire-jack-audio-connection-kit, reports a version >= 1.9.23 without
# actually declaring that function in its jack.h, which fails the build
# with "implicit declaration of function 'jack_max_cpu_load'". Probe for
# a real, working declaration instead of trusting the reported version.
Patch0: mod-desktop-fedora-jack-max-cpu-load.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake
BuildRequires: pkgconf-pkg-config
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: alsa-lib-devel
BuildRequires: portaudio-devel
BuildRequires: lilv-devel
BuildRequires: lv2-devel
BuildRequires: pkgconfig(jack)
BuildRequires: python3-devel
BuildRequires: desktop-file-utils
# The build's check-system-python target imports these at build time.
BuildRequires: python3-pillow
BuildRequires: python3-tornado
BuildRequires: python3-pycryptodomex
# Not in Fedora's own repositories; provided by the Audinux copr.
BuildRequires: python3-aggdraw

Requires: python3
Requires: python3-pillow
Requires: python3-tornado
Requires: python3-pycryptodomex
# Not in Fedora's own repositories; provided by the Audinux copr.
Requires: python3-aggdraw
Recommends: pipewire-jack-audio-connection-kit
Recommends: lv2

%description
MOD Desktop is a Qt system-tray application that starts and supervises
MOD's pedalboard engine (mod-host), MIDI routing (mod-midi-merger) and
web UI (mod-ui), opening the pedalboard editor in a browser tab.

This build uses the SYSTEM_DEPS=1 mode: it is compiled with the system
compiler against system Qt5/ALSA/PortAudio/LV2/lilv libraries and runs on
system Python packages, instead of PawPaw's bundled toolchain and
thirdparties. It connects standalone mod-host/mod-midi-merger clients to
an already-running JACK or PipeWire-JACK server (the Fedora default);
it does not bundle, start or stop a JACK server itself, and the bundled
plugin collection is not built — install LV2 plugins separately.

%prep
%autosetup -n %{name}-%{shortcommit0} -p1

%build
%set_build_flags

%make_build SYSTEM_DEPS=1 CC=%{__cc} CXX=%{__cxx}

%install
set -e

appdir=%{buildroot}%{_libexecdir}/%{name}

install -d -m 0755 "$appdir"
install -d -m 0755 "$appdir/mod" "$appdir/modtools"

# Qt tray launcher, JACK clients and MIDI tools
install -m 0755 build-system/src/systray/mod-desktop     "$appdir/mod-desktop"
install -m 0755 build-system/src/mod-host/mod-host        "$appdir/mod-host-native"
install -m 0755 build-system/midi/mod-midi-merger-standalone      "$appdir/mod-midi-merger"
install -m 0755 build-system/midi/mod-midi-broadcaster-standalone "$appdir/mod-midi-broadcaster"
install -m 0755 build-system/src/mod-utils/libmod_utils.so "$appdir/modtools/libmod_utils.so"

# Python helpers run as subprocesses by mod-desktop/mod-ui, named without a
# .py suffix so the sibling-binary lookups in utils/linux/system-host.py,
# mod/screenshot.py and the Qt launcher (AppProcess) find them by that name.
install -m 0644 utils/linux/system-host.py            "$appdir/mod-host.py"
install -m 0644 utils/cxfreeze/mod-ui-setup.py         "$appdir/mod-ui.py"
install -m 0644 utils/cxfreeze/mod-pedalboard-setup.py "$appdir/mod-pedalboard.py"
for helper in mod-host mod-ui mod-pedalboard; do
    cat > "$appdir/$helper" <<EOF
#!/bin/sh
cd -- "\$(dirname -- "\$0")" || exit 1
exec %{_bindir}/python3 ./$helper.py "\$@"
EOF
    chmod 0755 "$appdir/$helper"
done

# mod-ui's Python package, HTML UI and default pedalboard
cp -a src/mod-ui/mod/.      "$appdir/mod/"
cp -a src/mod-ui/modtools/. "$appdir/modtools/"
install -d -m 0755 "$appdir/html"
cp -a src/mod-ui/html/.     "$appdir/html/"
install -d -m 0755 "$appdir/default.pedalboard"
cp -a src/mod-ui/default.pedalboard/. "$appdir/default.pedalboard/"

# Factory pedalboards and misc metadata read relative to the binary
install -d -m 0755 "$appdir/pedalboards"
cp -a pedalboards/.                       "$appdir/pedalboards/"
install -m 0644 utils/linux/mod-hardware-descriptor.json "$appdir/mod-hardware-descriptor.json"
install -m 0644 VERSION                   "$appdir/VERSION"

find "$appdir/mod" "$appdir/modtools" "$appdir/html" \
     "$appdir/default.pedalboard" "$appdir/pedalboards" \
     -type d -exec chmod 0755 {} +
find "$appdir/mod" "$appdir/modtools" "$appdir/html" \
     "$appdir/default.pedalboard" "$appdir/pedalboards" \
     -type f -exec chmod 0644 {} +
chmod 0755 "$appdir/modtools/libmod_utils.so"

# Launcher in PATH; "exec"s the real binary by absolute path so dladdr()
# resolves the application directory to %{_libexecdir}/%{name}, regardless
# of how this wrapper itself was invoked.
install -d -m 0755 %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/sh
exec %{_libexecdir}/%{name}/%{name} "\$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/%{name}

# Desktop entry and icon
install -d -m 0755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Type=Application
Name=MOD Desktop
GenericName=Pedalboard
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Categories=AudioVideo;Audio;X-AudioEditing;Qt;
EOF
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m 0644 res/mod-logo.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files
%license LICENSE src/mod-host/COPYING src/mod-ui/LICENSE src/mod-midi-merger/LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Thu Oct 15 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.13.9717535-1
- initial spec: packages the SYSTEM_DEPS=1 Linux build from the 'fedora'
  branch of https://github.com/ycollet/mod-desktop (native Qt5/system
  JACK-PipeWire build, no PawPaw/bundled jackd), bundling mod-host and
  mod-midi-merger built from their pinned upstream commits and mod-ui from
  the 'fedora' branch of https://github.com/ycollet/mod-ui (Tornado 6
  compatibility fixes needed on current Fedora); everything is installed
  as a private, non-PATH bundle under %%{_libexecdir}/mod-desktop since the
  Qt launcher and mod-ui locate their sibling mod-host/mod-ui/pedalboards/
  html files relative to the running binary's own directory
- BuildRequires python3-pillow/tornado/pycryptodomex/aggdraw: the build's
  check-system-python target imports them directly, so they must be
  present in the build root too, not only at install time
- patch mod-host's Makefile (mod-desktop-fedora-jack-max-cpu-load.patch)
  to probe for a working jack_max_cpu_load() declaration instead of
  trusting jack.pc's reported version: Fedora's default JACK provider,
  pipewire-jack-audio-connection-kit, reports version >= 1.9.23 without
  declaring that function in its jack.h, which failed the build with an
  implicit-declaration error
