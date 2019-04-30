Name:       gstreamer1-libav
Version:    1.16.0
Release:    1%{?dist}
Epoch:      1
Summary:    GStreamer Libav plug-in
License:    LGPLv2+
URL:        https://gstreamer.freedesktop.org/modules/gst-libav.html

Source0:    http://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  orc-devel >= 0.4.16
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavcodec) >= 58
BuildRequires:  pkgconfig(libavutil)

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

%build
export CFLAGS="%{optflags} -Wno-error=attributes"
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
* Tue Apr 30 2019 Simone Caronni <negativo17@gmail.com> - 1:1.16.0-1
- Update to 1.16.0.

* Thu Apr 04 2019 Simone Caronni <negativo17@gmail.com> - 1:1.15.2-1
- Update to 1.15.2.
- Trim changelog.

* Sat Oct 20 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.4-1
- Update to 1.14.4.

* Wed Sep 26 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.3-1
- Update to 1.14.3.

* Thu Aug 30 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.2-1
- Update to 1.14.2.

* Thu Jun 14 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.1-1
- Update to 1.14.1.

* Wed May 02 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.0-1
- Update to 1.14.0.

* Wed May 02 2018 Simone Caronni <negativo17@gmail.com> - 1:1.12.4-2
- Switch to comaptibility FFMPeg (3.4).

* Tue Jan 09 2018 Simone Caronni <negativo17@gmail.com> - 1:1.12.4-1
- Update to 1.12.4.

* Sat Nov 18 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.3-3
- Temporary patch for FFMpeg 3.4 APIs.

* Wed Oct 25 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.3-2
- Rebuild for ffmpeg 3.4 update.

* Mon Oct 23 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.3-1
- Update to 1.12.3.

* Thu Jul 20 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.2-1
- Update to 1.12.2.

* Sat Jun 24 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.1-1
- Update to 1.12.1.

* Sat May 13 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.0-1
- Update to 1.12.0.

* Wed Apr 19 2017 Simone Caronni <negativo17@gmail.com> - 1:1.11.90-1
- Update to 1.11.90.
