#!/bin/bash
set -e

echo "[audio-topology] Detecting CPU topology..." >&2

lscpu -p=CPU,CORE,SOCKET,NODE,MAXMHZ | grep -v '^#'
