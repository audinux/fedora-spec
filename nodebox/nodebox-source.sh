#!/bin/bash
# Usage: ./nodebox-source.sh <TAG>
#        ./nodebox-source.sh v3.1.0
#
# This script clones NodeBox, downloads all Maven dependencies, builds the
# fat jar and resources, then packages everything into a source tarball
# suitable for rpmbuild.  An internet connection is required when running
# this script; the resulting tarball contains all pre-built artifacts so
# the RPM build itself can run offline (e.g. inside mock).

set -e

TAG=${1:-v3.1.0}
VERSION=${TAG#v}
PKGNAME=nodebox-${VERSION}

echo "==> Cloning NodeBox ${TAG} ..."
git clone https://github.com/nodebox/nodebox.git "${PKGNAME}"
cd "${PKGNAME}"
git checkout "${TAG}"

echo "==> Downloading Maven dependencies and building ..."
# 'archives' builds nodebox.jar (fat jar) and nodeboxlibs.zip
# 'resources' populates dist/unpacked/resources/
ant archives resources

echo "==> Removing bundled ffmpeg (system ffmpeg will be used) ..."
rm -f dist/unpacked/resources/bin/ffmpeg

echo "==> Packaging tarball ..."
cd ..

tar czf "${PKGNAME}.tar.gz" \
    "${PKGNAME}/dist/unpacked/" \
    "${PKGNAME}/artwork/nodebox-icon.svg" \
    "${PKGNAME}/artwork/nodebox-icon.png" \
    "${PKGNAME}/src/main/java/nodebox/client/Application.java"

rm -rf "${PKGNAME}"

echo "Done: ${PKGNAME}.tar.gz"
