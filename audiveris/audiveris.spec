# Status: active
# Tag: Editor
# Type: Standalone
# Category: Tool

Name: audiveris
Version: 5.10.2
Release: 1%{?dist}
Summary: Optical Music Recognition software
License: AGPL-3.0-or-later
URL: https://github.com/Audiveris/audiveris

BuildArch: noarch

Source0: app-%{version}.zip

Requires: java-25-openjdk
Requires: tesseract
Requires: tesseract-langpack-eng
Requires: freetype

%description
The goal of an OMR application is to allow the end-user to transcribe a score image into its symbolic counterpart.
This opens the door to its further use by many kinds of digital processing such as playback, music edition,
searching, republishing, etc.

The Audiveris application is built around the tight integration of two main components: an OMR engine and an OMR editor.
* The OMR engine combines many techniques, depending on the type of entities to be recognized -- ad-hoc methods for lines,
  image morphological closing for beams, external OCR for texts, template matching for heads, neural network for all
   other fixed-size shapes.
* Significant progresses have been made, especially regarding poor-quality scores, but experience tells us that a 100%
  recognition ratio is simply out of reach in many cases.
* The OMR editor thus comes into play to overcome engine weaknesses in convenient ways. The user can preselect processing
  switches to adapt the OMR engine before launching the transcription of the current score. Then the remaining mistakes
  can generally be quickly fixed via the manual editing of a few music symbols.

%prep

%autosetup -c

%install
unzip -o %SOURCE0

mkdir -p %{buildroot}/opt/
mv app-%{version} %{buildroot}/opt/audiveris

# wrapper
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/audiveris << 'EOF'
#!/bin/sh
exec /opt/audiveris/bin/Audiveris "$@"
EOF
chmod +x %{buildroot}%{_bindir}/audiveris

# cleanup
rm -f %{buildroot}/opt/audiveris/bin/Audiveris.bat

%files
/opt/audiveris/*
%{_bindir}/audiveris

%changelog
* Mon Mar 30 2026 Yann Collette <ycollette.nospam@free.fr> - 5.10.2-1
- initial spec
