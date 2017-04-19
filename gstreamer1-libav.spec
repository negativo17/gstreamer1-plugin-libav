Name:       gstreamer1-libav
Version:    1.11.90
Release:    1%{?dist}
Epoch:      1
Summary:    GStreamer Libav plug-in
License:    LGPLv2+
URL:        https://gstreamer.freedesktop.org/modules/gst-libav.html

Source0:    http://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  gstreamer1-devel >= 1.10.2
BuildRequires:  gstreamer1-plugins-base-devel >= 1.10.2
BuildRequires:  libtool
BuildRequires:  orc-devel >= 0.4.16
BuildRequires:  pkgconfig(libavfilter) >= 3.2
BuildRequires:  pkgconfig(libavformat) >= 3.2
BuildRequires:  pkgconfig(libavcodec) >= 3.2
BuildRequires:  pkgconfig(libavutil) >= 3.2
BuildRequires:  pkgconfig(libswscale) >= 3.2

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
export CFLAGS="%{optflags} -Wno-deprecated-declarations"
autoreconf -vif
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-orc \
    --with-package-name="Fedora GStreamer-libav package" \
    --with-package-origin="http://negativo17.org" \
    --with-system-libav
make %{?_smp_mflags}

%install
%make_install
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
* Wed Apr 19 2017 Simone Caronni <negativo17@gmail.com> - 1:1.11.90-1
- Update to 1.11.90.

* Mon Dec 05 2016 Simone Caronni <negativo17@gmail.com> - 1:1.10.2-1
- Update to 1.10.2.

* Mon Nov 28 2016 Simone Caronni <negativo17@gmail.com> - 1:1.10.1-1
- Update to 1.10.1.

* Thu Nov 10 2016 Simone Caronni <negativo17@gmail.com> - 1:1.10.0-1
- Update to 1.10.0.
- Requires FFmpeg >= 3.2.

* Wed Nov 09 2016 Simone Caronni <negativo17@gmail.com> - 1:1.9.2-2
- Rebuild for FFmpeg update.

* Thu Nov 03 2016 Simone Caronni <negativo17@gmail.com> - 1:1.9.2-1
- Update to 1.9.2.

* Wed Aug 17 2016 Simone Caronni <negativo17@gmail.com> - 1:1.9.1-1
- Update to 1.9.1.

* Mon Jul 25 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.2-3
- Fix devel-docs requirements.

* Thu Jul 21 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.2-2
- Rebuild for FFMpeg 3.1.1.

* Mon Jun 13 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.2-1
- First build.
