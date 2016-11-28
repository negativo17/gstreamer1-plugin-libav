Name:       gstreamer1-libav
Version:    1.8.3
Release:    3%{?dist}
Epoch:      1
Summary:    GStreamer Libav plug-in
License:    LGPLv2+
URL:        https://gstreamer.freedesktop.org/modules/gst-libav.html

Source0:    http://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz

Patch0:     0001-Only-use-AV_CODEC_ID_WRAPPED_AVFRAME-on-new-enough-l.patch
Patch1:     0002-libav-Update-to-ffmpeg-n3.0.3.patch
Patch2:     0003-av-Cast-AVContext-bit_rate-to-a-guint-before-passing.patch
Patch3:     0004-libav-Update-to-ffmpeg-n3.0.4.patch
Patch4:     0005-avaudenc-dec-Ignore-S64BE-LE-pseudo-codecs.patch
Patch5:     0006-avaudenc-dec-Allow-compilation-against-ffmpeg-3.2-ag.patch
Patch6:     0007-configure-fix-target_os-when-cross-compiling-for-arm.patch
Patch7:     0008-avvidenc-dec-Disable-more-hardware-encoder-decoders.patch
Patch8:     0009-avmux-blacklist-fifo-plugin.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  gstreamer1-devel >= 1.8.0
BuildRequires:  gstreamer1-plugins-base-devel >= 1.8.0
BuildRequires:  libtool
BuildRequires:  orc-devel >= 0.4.16
BuildRequires:  pkgconfig(libavfilter) >= 3.0.2
BuildRequires:  pkgconfig(libavformat) >= 3.0.2
BuildRequires:  pkgconfig(libavcodec) >= 3.0.2
BuildRequires:  pkgconfig(libavutil) >= 3.0.2
BuildRequires:  pkgconfig(libswscale) >= 3.0.2

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
%autosetup -n gst-libav-%{version}

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
* Mon Nov 28 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.3-3
- Add patches from 1.8 branch.

* Wed Nov 09 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.3-2
- Rebuild for FFmpeg update.

* Mon Aug 22 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.3-1
- Update to 1.8.3.

* Mon Jul 25 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.2-3
- Fix devel-docs requirements.

* Thu Jul 21 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.2-2
- Rebuild for FFMpeg 3.1.1.

* Mon Jun 13 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.2-1
- First build.
