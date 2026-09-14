#!/bin/bash

set -euo pipefail

VENDOR_DIR="vendor"
ARCHIVE="Cagire-vendor.tar.xz"

if [ ! -f Cargo.toml ]; then
    echo "ERROR: Cargo.toml not found."
    echo "Run this script from the root of the Cagire source tree."
    exit 1
fi

if [ ! -f Cargo.lock ]; then
    echo "ERROR: Cargo.lock not found."
    exit 1
fi

echo "==> Checking for git dependencies from git.raphaelforment.fr"

if grep -q 'git.raphaelforment.fr' Cargo.lock; then
    grep -B2 -A2 'git.raphaelforment.fr' Cargo.lock
else
    echo "WARNING: no dependency from git.raphaelforment.fr found."
fi

echo
echo "==> Removing previous vendor directory"

rm -rf "$VENDOR_DIR"

echo
echo "==> Running cargo vendor"

cargo vendor --locked "$VENDOR_DIR"

echo
echo "==> Checking vendored dependencies"

if [ ! -d "$VENDOR_DIR" ]; then
    echo "ERROR: cargo vendor did not create $VENDOR_DIR"
    exit 1
fi

if find "$VENDOR_DIR" -type f -print0 |
   xargs -0 grep -l 'git.raphaelforment.fr' >/dev/null 2>&1
then
    echo "WARNING: git URL found in vendored files."
fi

echo
echo "==> Creating archive"

rm -f "$ARCHIVE"

tar -cJf "$ARCHIVE" "$VENDOR_DIR"

echo
echo "==> Done"
echo
echo "Generated:"
echo "  $VENDOR_DIR/"
echo "  $ARCHIVE"
echo
echo "Archive size:"
du -h "$ARCHIVE"

echo
echo "==> Cargo configuration"

echo "cargo vendor normally prints the configuration required for"
echo "offline builds above. Copy the generated [source.*] configuration"
echo "to .cargo/config.toml if it is not already present."

