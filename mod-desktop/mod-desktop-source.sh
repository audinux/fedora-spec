#!/bin/bash
#
# ./mod-desktop-source.sh
#
# Assembles the mod-desktop source tarball used by mod-desktop.spec.
#
# mod-desktop's "SYSTEM_DEPS=1" Linux build (added on the 'fedora' branch of
# https://github.com/ycollet/mod-desktop) needs sibling sources for mod-host
# and mod-midi-merger (normally git submodules), plus a Tornado-6-compatible
# mod-ui checkout (the 'fedora' branch of https://github.com/ycollet/mod-ui,
# used in place of the release-pinned mod-ui submodule, which only supports
# Tornado 4). PawPaw, DPF, mod-plugin-builder and mod-desktop-asio are not
# used by this build mode and are intentionally left out to keep the
# tarball small and avoid an unused Wine/ASIO dependency.
#
# This script performs all network access up front, so rpmbuild/mock never
# need network access to build mod-desktop.spec.

set -euo pipefail

# Keep these in sync with the %%global commit pins in mod-desktop.spec.
MOD_DESKTOP_REPO=${MOD_DESKTOP_REPO:-https://github.com/ycollet/mod-desktop.git}
MOD_DESKTOP_COMMIT=${MOD_DESKTOP_COMMIT:-97175358035d5e96332b44e95ed62d23a4fdf08e}

MOD_UI_REPO=${MOD_UI_REPO:-https://github.com/ycollet/mod-ui.git}
MOD_UI_COMMIT=${MOD_UI_COMMIT:-93e1a04f107d0290fe457d886bff5c57cf1d465c}

MOD_HOST_REPO=${MOD_HOST_REPO:-https://github.com/mod-audio/mod-host.git}
MOD_HOST_COMMIT=${MOD_HOST_COMMIT:-754070f94bffafb51c7f3d86df47bc04b00f1151}

MOD_MIDI_MERGER_REPO=${MOD_MIDI_MERGER_REPO:-https://github.com/mod-audio/mod-midi-merger.git}
MOD_MIDI_MERGER_COMMIT=${MOD_MIDI_MERGER_COMMIT:-db24bd754ff01134e5eca0fb7a5ec188eab2e329}

SHORTCOMMIT=${MOD_DESKTOP_COMMIT:0:7}
WORKDIR="mod-desktop-${SHORTCOMMIT}"

fetch_at() {
    local repo="$1" commit="$2" destdir="$3"

    git clone --quiet "$repo" "$destdir"
    if ! git -C "$destdir" checkout --quiet "$commit"; then
        echo "Wrong commit / branch / tag: $commit ($repo)"
        exit 1
    fi
}

rm -rf "$WORKDIR"

fetch_at "$MOD_DESKTOP_REPO" "$MOD_DESKTOP_COMMIT" "$WORKDIR"

# Populate the submodule paths the SYSTEM_DEPS build actually needs, in
# place of 'git submodule update' (which would also pull PawPaw/DPF/etc).
rm -rf "$WORKDIR/src/mod-host" "$WORKDIR/src/mod-midi-merger" "$WORKDIR/src/mod-ui"
fetch_at "$MOD_HOST_REPO" "$MOD_HOST_COMMIT" "$WORKDIR/src/mod-host"
fetch_at "$MOD_MIDI_MERGER_REPO" "$MOD_MIDI_MERGER_COMMIT" "$WORKDIR/src/mod-midi-merger"
fetch_at "$MOD_UI_REPO" "$MOD_UI_COMMIT" "$WORKDIR/src/mod-ui"

find "$WORKDIR" -name .git -exec rm -rf {} +
find "$WORKDIR" -name .gitmodules -delete
find "$WORKDIR" -name .gitignore -delete

tar cvfz "$WORKDIR.tar.gz" "$WORKDIR"
rm -rf "$WORKDIR"
sha256sum "$WORKDIR.tar.gz"
