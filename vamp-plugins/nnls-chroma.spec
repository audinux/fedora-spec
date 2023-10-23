# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: nnls-chroma
Version: 1.1
Release: 2%{?dist}
Summary: NNLS Chroma analyses a single channel of audio using frame-wise spectral input from the Vamp host
License: GLPv2
URL: http://www.isophonics.net/nnls-chroma

Vendor:       Audinux
Distribution: Audinux

Source0: https://code.soundsoftware.ac.uk/attachments/download/1691/nnls-chroma-%{version}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: vamp-plugin-sdk-devel
BuildRequires: boost-devel

%description
NNLS Chroma analyses a single channel of audio using frame-wise spectral
input from the Vamp host. The plugin was originally developed to extract
treble and bass chromagrams for subsequent use in chord extraction methods.
The spectrum is transformed to a log-frequency spectrum (constant-Q)
with three bins per semitone. On this representation, two processing
steps are performed:
* tuning, after which each centre bin (i.e. bin 2, 5, 8, …) corresponds
  to a semitone, even if the tuning of the piece deviates from 440 Hz
  standard pitch.
* running standardisation: subtraction of the running mean, division by
  the running standard deviation. This has a spectral whitening effect.

The processed log-frequency spectrum is then used as an input for NNLS
approximate transcription (using a dictionary of harmonic notes with
geometrically decaying harmonics magnitudes). The output of the NNLS
approximate transcription is semitone-spaced. To get the chroma, this
semitone spectrum is multiplied (element-wise) with the desired profile
(chroma or bass chroma) and then mapped to 12 bins. The resulting chroma
frames can be normalised by (dividing by) their norm (L1, L2 and maximum
norm available).

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
NNLS Chroma analyses a single channel of audio using frame-wise spectral
input from the Vamp host. The plugin was originally developed to extract
treble and bass chromagrams for subsequent use in chord extraction methods.
The spectrum is transformed to a log-frequency spectrum (constant-Q)
with three bins per semitone. On this representation, two processing
steps are performed:
* tuning, after which each centre bin (i.e. bin 2, 5, 8, …) corresponds
  to a semitone, even if the tuning of the piece deviates from 440 Hz
  standard pitch.
* running standardisation: subtraction of the running mean, division by
  the running standard deviation. This has a spectral whitening effect.

The processed log-frequency spectrum is then used as an input for NNLS
approximate transcription (using a dictionary of harmonic notes with
geometrically decaying harmonics magnitudes). The output of the NNLS
approximate transcription is semitone-spaced. To get the chroma, this
semitone spectrum is multiplied (element-wise) with the desired profile
(chroma or bass chroma) and then mapped to 12 bins. The resulting chroma
frames can be normalised by (dividing by) their norm (L1, L2 and maximum
norm available).

%prep
%autosetup

sed -i -e "/ARCHFLAGS =/d" Makefile.linux
sed -i -e "s/CFLAGS += \$(ARCHFLAGS)/CFLAGS += \$(ARCHFLAGS) \$(SPECCFLAGS)/g" Makefile.linux
sed -i -e "s/CXXFLAGS += \$(ARCHFLAGS)/CXXFLAGS += \$(ARCHFLAGS) \$(SPECCXXFLAGS)/g" Makefile.linux

%build

%set_build_flags
export SPECCFLAGS="$CFLAGS"
export SPECXXCFLAGS="$CXXFLAGS"

%make_build -f Makefile.linux

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 nnls-chroma.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 nnls-chroma.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 nnls-chroma.n3  %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%license COPYING
%doc README
%{_libdir}/vamp/nnls-chroma.*

%changelog
* Fri Jul 22 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1-2
- update to 1.1-2

* Sat Jan 08 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1-1
- Initial spec file

