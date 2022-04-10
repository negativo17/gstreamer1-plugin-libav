Name:       gstreamer1-libav
Version:    1.14.5
Release:    2%{?dist}
Epoch:      1
Summary:    GStreamer Libav plug-in
License:    LGPLv2+
URL:        https://gstreamer.freedesktop.org/modules/gst-libav.html

Source0:    http://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz
Patch0:     %{name}-temp-ffmpeg-3.4-api.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  orc-devel >= 0.4.16
BuildRequires:  pkgconfig(libavfilter) >= 7
BuildRequires:  pkgconfig(libavfilter) < 8
BuildRequires:  pkgconfig(libavformat) >= 58
BuildRequires:  pkgconfig(libavformat) < 59
BuildRequires:  pkgconfig(libavcodec) >= 58
BuildRequires:  pkgconfig(libavcodec) < 59
BuildRequires:  pkgconfig(libavutil) >= 56
BuildRequires:  pkgconfig(libavutil) < 57

%ifarch %{ix86} x86_64
BuildRequires:  yasm
%endif

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

GStreamer Libav plug-in contains one plugin with a set of elements using the
Libav library code. It contains many popular decoders and encoders.


%package devel-docs
Summary:    Development documentation for the GStreamer Libav plug-in
Requires:   %{name} = %{?epoch}:%{version}-%{release}
BuildArch:  noarch

%description devel-docs
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development documentation for the GStreamer Libav
plug-in.

%prep
%autosetup -p1 -n gst-libav-%{version}
sed -i -e 's/-Wno-portability 1.14/-Wno-portability 1.13/g' configure.ac

%build
export CFLAGS="%{optflags} -Wno-deprecated-declarations"
autoreconf -vif
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-gtk-doc \
    --enable-orc \
    --with-package-name="Fedora GStreamer-libav package" \
    --with-package-origin="http://negativo17.org" \
    --with-system-libav
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%files
%license COPYING.LIB
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/gstreamer-1.0/libgstlibav.so

%files devel-docs
# Take the dir and everything below it for proper dir ownership
%doc %{_datadir}/gtk-doc

%changelog
* Sun Apr 10 2022 Simone Caronni <negativo17@gmail.com> - 1:1.14.5-2
- Rebuild for updated dependencies.

* Mon Jul 13 2020 Simone Caronni <negativo17@gmail.com> - 1:1.14.5-1
- Update to 1.14.5.

* Mon Jun 29 2020 Simone Caronni <negativo17@gmail.com> - 1:1.14.4-2
- Rebuild for updated dependencies.

* Mon Nov 11 2019 Simone Caronni <negativo17@gmail.com> - 1:1.14.4-1
- Rebase to 1.14.4.

* Wed May 02 2018 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-4
- Switch to comaptibility FFMPeg (3.4).

* Sat Nov 18 2017 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-3
- Temporary patch for FFMpeg 3.4 APIs.

* Wed Oct 25 2017 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-2
- Rebuild for ffmpeg 3.4 update.

* Wed Aug 16 2017 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-1
- Update to 1.10.4.

* Thu Nov 10 2016 Simone Caronni <negativo17@gmail.com> - 1:1.4.5-3
- Require compat-ffmpeg (2.8.8).

* Wed Nov 09 2016 Simone Caronni <negativo17@gmail.com> - 1:1.4.5-2
- Rebuild for FFmpeg update.

* Wed Aug 17 2016 Simone Caronni <negativo17@gmail.com> - 1:1.4.5-1
- First build.
