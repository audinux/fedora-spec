# Tag: Editor, Graphic
# Type: Standalone, IDE, Language
# Category: Graphic, Tool

%global _version 2.31-1

Name: mandelbulber2
Version: 2.31
Release: 1%{?dist}
License: GPL-3.0
Summary: 3D Mandelbrot renderer
URL: https://mandelbulber.com/

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/buddhi1980/mandelbulber2/releases/download/%{_version}/mandelbulber2-%{_version}.tar.gz#/%{name}-%{_version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: gsl-devel
BuildRequires: libtiff-devel
BuildRequires: libpng-devel
BuildRequires: lzo-devel
BuildRequires: libsndfile-devel
BuildRequires: desktop-file-utils

%description
Easy to use, handy but experimental application designed to help
you render 3D Mandelbrot fractals called Mandelbulb and some other
kind of 3D fractals like Mandelbox, Bulbbox, Juliabulb, Menger
Sponge.

%prep
%autosetup -n %{name}-%{_version}

%build

cd makefiles
%qmake_qt5 mandelbulber.pro
%make_build

%install

install -Dm0755 makefiles/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm0644 qt/icons/mandelbulber.png %{buildroot}%{_datadir}/pixmaps/mandelbulber.png

# install usr content
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
cp -a usr/share/%{name}/* %{buildroot}%{_datadir}/%{name}/
cp -a usr/share/doc/%{name}/Mandelbulber_Manual.pdf %{buildroot}%{_datadir}/doc/%{name}/

sed -i -e "s/Graphics;3DGraphics;Math;Science/Graphics/g" %{buildroot}/%{_datadir}/applications/%{name}.desktop

desktop-file-install                         \
  --add-category="Graphics"		     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc NEWS README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/%{name}/Mandelbulber_Manual.pdf
%{_datadir}/pixmaps/mandelbulber.png
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/data/*
%{_datadir}/%{name}/examples/*
%{_datadir}/%{name}/formula/*
%{_datadir}/%{name}/icons/*
%{_datadir}/%{name}/language/*
%{_datadir}/%{name}/materials/*
%{_datadir}/%{name}/opencl/*
%{_datadir}/%{name}/scripts/*
%{_datadir}/%{name}/sounds/*
%{_datadir}/%{name}/textures/*
%{_datadir}/%{name}/toolbar/*

%changelog
* Mon Jul 10 2023 Yann Collette <ycollette.nospam@free.fr> - 2.30-1
- update to 2.30-1

* Sun Apr 09 2023 Yann Collette <ycollette.nospam@free.fr> - 2.29-1
- update to 2.29-1

* Fri Jul 15 2022 Yann Collette <ycollette.nospam@free.fr> - 2.28-1
- update to 2.28-1

* Fri Feb 18 2022 Yann Collette <ycollette.nospam@free.fr> - 2.27-1
- update to 2.27-1

* Fri Nov 5 2021 Yann Collette <ycollette.nospam@free.fr> - 2.26-1
- update to 2.26-1

* Wed Aug 05 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2.22
- Rebuilt for Fedora
* Sat Jun  6 2015 malcolmlewis@opensuse.org
- Updated to version 2.04:
  + Added ray-traced transparency and Fresnel's refraction.
  + Added NetRender   + rendering of the same image or animation on
    multiple machines over the TCP/IP network (Internet, local
    LAN).
  + Shading of DOF parallelized via OpenMP (leverages shading time
    roughly about 1/3 on an 8 core CPU).
  + Added boolean functions for fractal formulas.
  + added transform functions for fractal formulas (useful for
    boolean operations).
  + Added several fractal formulas.
  + Added box and spherical folding.
  + More ergonomic layout for IFS formula.
  + Added log window (information dock).
  + Added histogram view.
  + Application settings are saved when application is shut down.
  + Fixed bug: saved jpeg images where corrupted when width was not
    multiply of 4.
  + Fixed bug: there was noise when "stop at maximum iteration"
    mode was enabled.
  + Source code repository moved to
    http://github.com/buddhi1980/mandelbulber2.
  + Fixed bug: corrected calculation of coordinates of 3D cursor
    when there was used 3-point perspective.
- Changes from version 2.0.3-1:
  + Fixed bug: improper loading of "old settings" when system used
    comma as decimal separator.
- Changes from version 2.03:
  + Added recording and rendering of flight animation. All frames
    are displayed in the table with previews.
  + There is possible to edit values in the table and interpolate
    them in selected range of frames.
  + All frames can be edited in any spreadsheet editor. CSV format
    is used in settings file to store animation frames.
  + There is possible to add any parameter to animation (context
    menu for every parameter).
  + Added keyboard shortcuts for recording (pause, strafe, roll).
  + Added player for animation (plays directly from sequence of jpg
    files).
  + Added user defined toolbar. To add new preset it's enough to
    save settings to $HOME/.mandelbulber/toolbar folder.
  + Added quit confirmation dialog.
  + Added multiple language support (EN, PL, DE).
  + Reduced all margins and spacings in UI.
  + Added automatic tabify of docks when application is started
    first time.
  + In file selection dialog the preview is rendered much faster.
  + Added missing mandelbulber.png icon.
  + More detailed recording of errors in .mandelbulber_log.txt.
  + Corrected tab order in UI.
  + Fixed bug: in install script.
  + Fixed bug: there was double slash in paths for files.
  + Fixed bug: after application quit rendering was not terminated.
- Changes from version 2.02:
  + Added importing of settings from old Mandelbulber (v1.21). It
    works in 95%% cases.
  + Added 'legacy_coordinate_system' parameter to provide
    compatibility with old coordinate system (upside down).
  + Added primitive objects: box, sphere, plane, cylinder, torus,
    circle, rectangle, water. There is no limit for number of
    objects. All objects can be rotated around 3 axes and placed
    using mouse pointer.
  + Added 'repeat' operator for all primitive objects and fractal.
  + Added setting for position and rotation of the fractal.
  + Added example setting files and 'Load example...' option.
  + Added crossplatform consistent random number generator based on
    the gsl library. See the README for new dependencies.
  + Fixed bug: 'fractal_constant_factor' parameter was ignored.
  + Fixed bug: glow effect used wrong color.
  + Fixed bug: there was error in calculation of equirectangular
    projection.
  + Fixed bug: corrected and updated list of required system
    packages.
  + Fixed bug: there was wrong calculation of distance if
    "Iteration threshold mode" was enabled.
  + Fixed bug: preview was displayed even if settings weren't
    loaded successfully.
- Changes from version 2.01:
  + migrated to Qt 5   + program in 99%% rewriten from scratch.
  + Note: Program still under development. Not available yet:
    NetRender, animation, OpenCL, and many other small features.
- Changes from version 1.21-2:
  + fixed bug: OpenCL   + name of variable 'half' was restricted
    and caused compiler errors.
- Add mandelbulber-fix-build-with-libpng12.patch: Fix building with
  libpng12.
- Add mandelbulber-fix-desktop-file.patch Remove path to icon file
  and icon extension.
- Add mandelbulber.changes as source, as it's used during build to
  inject the last change date / time into the build.
* Mon Jun  9 2014 malcolmlewis@cableone.net
- Updated to version 1.21-1:
  + Fixed bug: OpenCL - SSAO kernel coudn't be compiled on nVidia.
  + Fixed bug: OpenCL - there was error -54 during rendering of
    SSAO and DOF (caused by not matched localWorkSize with
    GlobalWorkSize).
- Updates fro version 1.21:
  + Added color palette editor.
  + Added function to convert flight path into keyframes.
  + Improved water algorithm - less visible pattern.
  + Added setting for water animation speed.
  + In flight path recording function added switching between using
    gamma rotation or not (use "Rotate without using gamma angle").
  + In flight path recording function added switching between
    constant flight speed and based on estimated distance (use
    "Absolute distance mode").
  + Added arrows in HUD for flight path recording.
  + Added low quality SSAO effect during progressive rendering
    (better looking fast preview).
  + Optimized binary searching algorithm in RayMarching() function.
  + OpenCL - added kernel for Screen Space Ambient Occlusion (SSAO)
    effect.
  + OpenCL - added kernel for Depth Of Field (DOF) effect. There is
    possible to switch between Monte-Carlo DOF and post-effect DOF.
  + OpenCL - improved quality of "fake lights" based on orbit
    traps.
  + OpenCL - implemented textured background.
  + OpenCL - added alpha channel in "Full" kernel (possible to save
    image as PNG-16 + Alpha).
  + Fixed bug: flight path rendering didn't worked properly when
    rendering was continued from the middle.
  + Fixed bug: eliminated memory leaks in OpenCL rendering
    functions.
  + Fixed bug: corrected calculation of viewVector and z value for
    3-point perspective.
  + Fixed bug: sometimes 3D cursor was jerky. Added temporary
    disabling for event handler during rendering of cursor.
- Updates from version 1.20:
  + OpenCL - added NoDE rendering engine.
  + OpenCL - added "limits" feature to rendering engine.
  + OpenCL - added "interior mode".
  + OpecCL - added primitive objects.
  + OpenCL - next trial to fix the problem with -I option for
    OpenCL compiler (spaces in path were not passed properly).
  + OpenCL - added setting for delta for deltaDE algorythm.
  + Added HUD for flight path recording.
  + Simplified code and corrected for "limits" and "interior mode".
  + Fixed problem with visibility of 3D cursor during flight path
    recording.
  + Fixed resource leaks
- Updates from version 1.19:
  + OpenCL - added management for user defined formulas.
  + Added showing of light animation paths in image window.
  + Improved algorithm for fake lights based on orbit traps.
  + OpenCL - implemented fake lights in "full" kernel.
  + OpenCL - added error handling and messages for most of errors.
    Program is not terminated when error occurs
  + OpenCL - added setting for max GPU memory intented to use with
    OpenCL. Can be helpful when program cannot detect avilable
    memory.
  + Added quit confirmation dialog.
  + OpenCL - added selection for OpenCL platform, device and
    switching between use of GPU or CPU.
  + Added loading at program startup and saving at program exit of
    several application settings.
  + Added error handling for lack of memory errors.
  + Fixed bug: when in NetRender the client was enabled there was
    not possible to close the program
  + Fixed bug: applied patches for memory leaks.
* Tue Oct 15 2013 malcolmlewis@opensuse.org
- Updated to version 1.18:
  + Added 3D pointer in image preview window.
  + Added showing of animation path in image preview window.
  + Fixed bug: lights were placed in wrong position on fish-eye
    mode.
- Updates from version 1.17:
  + Animation record mode works now like flight simulator. There
    is also recorded camera gamma angle.
  + Added HDR filter.
  + Fixed bug: there was vissible different detail level between
    3-point perspective and fish-eye.
  + Fixed bug: Netrender didn't work with number of tiles > 1.
* Wed Aug  7 2013 malcolmlewis@opensuse.org
- Updated to Version 1.16:
  + All shaders and rendering engine rewritten from the beginning.
  + Light sources are rendered as a volumetric objects.
  + Introduced soft shadows.
  + Raytracing works with all shaders and is much more accurate.
  + Glow and all fog shaders now are volumetric effects and can be
    used simultanously.
  + Possible to set different reflection factor for each primitive
    object.
  + Zoom by click works much more accurate and rotates the camera
    towards to selected point.
  + Added option for using constant step length for zoom by click
    (useful for animations).
  + Added contrast adjustment for image.
  + User interface reorganized.
  + Internal image buffer is now floating point type (better HDR
    effects).
  + Fixed bug: crashed when animation keyframe thumbnail was
    refrshed during image rendering.
  + Fixed bug: NetRender client saved partially rendered images.
  + Fixed bug: animated water wasn't rendered properly with
    NetRender.
  + Remark: some shaders settings are not compatible with older
    setting files (fog and DOF distance, reflection factor).
* Fri May  3 2013 malcolmlewis@opensuse.org
- Updated to Version 1.15:
  + Added light sources based on orbit traps.
  + Added NetRender client in noGUI mode.
* Mon Mar  4 2013 malcolmlewis@opensuse.org
- Updated to Version 1.13:
  + NetRender added.
  + Fix memory leaks.
  + Fixed bug: program crashed during DOF rendering. Randomizing
    function produced aritmetic fatal errors.
  + DOF - improved image refreshing for large images (better
    rendering performance).
* Sat Sep 15 2012 malcolmlewis@opensuse.org
- Updated to Version 1.12:
  + Fixed bug: background texture was not seamless.
  + Fixed bug: some of shadows in volumatric iteration fog weren't
  calculated properly.
  + Added saving of all image layers in separate PNG 16-bit files.
  + Improved fish eye perspective projection - now is compatible
  with full-dome projectors.
  + Added "fish eye 180 degree cut" mode to limit rendering area to
  hemisphere.
* Fri Apr 13 2012 malcolmlewis@opensuse.org
- Updated to Version 1.11:
  + Added iteration fog effect (fog which density depends on
    interation count). This fog cast shadows on fractal surface
    and on itself. Can be also iluminated by auxiliary lights
    and ambiet occlusion.
  + Improved water animation effect.
  + Disabling of SSAO and DOF when tile rendering is enabled.
  + OpenCL: added ambient occlusion effect.
  + OpenCL: added colouring algorithms.
  + OpenCL: added setting for OpenCL job size.
  + OpenCL: added new rendering engine "Crazy: iteration fog
    count".
  + OpebCL: added Quaternion and Xonodreambuie formulas.
  + OpenCL: added volumetric fog effect.
  + Fixed bug: thumbanils weren't rendered properly.
  + Fixed bug: weird colour gradients (http://www.fractalforums.
    com/index.php?topic=10305.msg41172#msg41172).
  + Added few example files for "iteration fog" effect.
* Fri Jan  6 2012 malcolmlewis@opensuse.org
- Updated to Version 1.10:
  + Added tile renderig (without any image resolution
    limitations).
  + Fixed bug: water animation worked only in flight mode.
* Sun Dec 18 2011 malcolmlewis@opensuse.org
- Updated to Version 1.09:
  + Implemented OpenCL support (now only under linux) for image
    preview. Works only for few formulas.
  + Added formula General Fold Box (reference: http://www.
    fractalforums.com/new-theories-and-research/generalized-box
  - fold/msg36503/#msg36503).
  + Fixed rotation problems in aminations. Patch by mintaka
    (http://www.fractalforums.com/mandelbulber/mandelbulber-1
  - 06-patch/).
  + Added animation effect for water.
- Update spec file License field from GPLv3 to GPL-3.0+ to
  conform with spdx.org identifier.
* Sun Oct 23 2011 malcolmlewis@opensuse.org
- Updated to Version 1.08:
  + Impelemnted primitive objects like plane, box, sphere and
    water.
  + Improved raytraced reflections algorithm - better reflections
    with ambient occlusion.
  + Added fast ambient occlusion effect. Reference:
    http://www.iquilezles.org/www/material/nvscene2008/rwwtt.pdf
    (Iñigo Quilez – iq/rgba).
  + Added possibility to turn off "penetrating light" for the main
    light source.
  + Added function for auto-calculate of fog parameters.
  + Added coordinates and distance measurement tool.
- Updates from Version 1.07:
  + Added reset button on IFS tab.
  + Removed some further limitations for image size.
  + Image brightness adjustment affects now on all image layers.
  + Added saturation adjustment for random colour palette.
  + Added volumetric fog effect.
  + Corrected displaying of image size in MegaBytes when size is
    greater than 2GB.
  + Changed shaders sequence. Glow looks better when fog (from
    post-processing) is enabled.
- Updates from Version 1.061:
  + Cretated 64-bit version for Windows (based on experimental
    versio of GTK+ libraries).
  + Fixed bug: Removed many uninitialised variables (found using
    valgrind).
  + Fixed problem with -lowmem mode (reported on
    http://www.fractalforums.com/mandelbulber/(1-06)-lowmem-switch
  - causes-segfaults-when-increasing-resolution/
    msg34210/#msg34210).
  + Fixed bug: overflow in UpdatePreviewSettingsDialog().
- Updates from Version 1.06:
  + Added possibility to render MengerKoch formula. It is added as
    an option for IFS formula (Menger Sponge mode; edge x,y,z).
  + Corrected ray-tracing algorithm. Fog and specular highlights
    weren't calculated properly in reflections.
  + Fixed problem in CalculateNormals() function. Sometimes when
    all deltas were zero, it produced NaN value. It caused white
    dots in raytraced reflections.
  + Added many simple formulas for hybryd sequence: x^2/(x + p);
    y^2/(y + p); z^2/(z + p); r^2/(r + p); spherical fold; x^p,
    y^p, z^p; x * p; y * p; z * p; x + p; y + p; z + p; axis X
    angle multiply by p; axis Y angle multiply by p; axis Z angle
    multiply by p.
  + Improved quality of raytraced reflections by adding binary
    searching in DE algorithm.
* Sat Oct 22 2011 malcolmlewis@opensuse.org
- Desktop file and icon added.
* Sat Oct 22 2011 malcolmlewis@opensuse.org
- Initial build.
