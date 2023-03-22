#!/bin/sh
# Make sure xsimd is still compatible with pythran
pythran minimal.py -DUSE_XSIMD -march=native
