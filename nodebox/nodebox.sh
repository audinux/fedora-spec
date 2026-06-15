#!/bin/bash
# Launcher for NodeBox.
# The fat jar has Main-Class set in its manifest; FileUtils.getApplicationFile()
# locates resources/ by navigating two directory levels above the jar, so the
# installation layout must be:
#   /usr/share/nodebox/lib/nodebox.jar
#   /usr/share/nodebox/resources/...
exec java -jar %{_datadir}/nodebox/lib/nodebox.jar "$@"
