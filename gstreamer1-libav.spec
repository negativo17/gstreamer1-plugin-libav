Name:       gstreamer1-libav
Version:    1.4.5
Release:    2%{?dist}
Epoch:      1
Summary:    GStreamer Libav plug-in
License:    LGPLv2+
URL:        https://gstreamer.freedesktop.org/modules/gst-libav.html

Source0:    http://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  gstreamer1-devel >= 1.4.0
BuildRequires:  gstreamer1-plugins-base-devel >= 1.4.0
BuildRequires:  libtool
BuildRequires:  orc-devel >= 0.4.16
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)

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
%setup -q -n gst-libav-%{version}

%build
autoreconf -vif
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-orc \
    --with-package-name="Fedora GStreamer-libav package" \
    --with-package-origin="http://negativo17.org" \
    --with-system-libav
make %{?_smp_mflags} V=1

%install
%make_install V=1
find %{buildroot} -name "*.la" -delete

%files
%{!?_licensedir:%global license %%doc}
%license COPYING.LIB
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/gstreamer-1.0/libgstlibav.so

%files devel-docs
# Take the dir and everything below it for proper dir ownership
%doc %{_datadir}/gtk-doc

%changelog
* Wed Nov 09 2016 Simone Caronni <negativo17@gmail.com> - 1:1.4.5-2
- Rebuild for FFmpeg update.

* Wed Aug 17 2016 Simone Caronni <negativo17@gmail.com> - 1:1.4.5-1
- First build.
