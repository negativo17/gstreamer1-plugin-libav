Name:       gstreamer1-plugin-libav
Version:    1.16.1
Release:    3%{?dist}
Epoch:      1
Summary:    GStreamer Libav plug-in
License:    LGPLv2+
URL:        https://gstreamer.freedesktop.org/modules/gst-libav.html

Source0:    http://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz
Patch0:     https://gitlab.freedesktop.org/gstreamer/gst-libav/-/commit/801dc93b790e9a96aa437a3f344214170c0bd540.diff

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
BuildRequires:  python3

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
    --with-package-origin="https://negativo17.org" \
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
* Mon Jun 17 2024 Simone Caronni <negativo17@gmail.com> - 1:1.16.1-3
- Switch to FFmpeg 5+.

* Tue Feb 07 2023 Simone Caronni <negativo17@gmail.com> - 1:1.16.1-2
- First build for el8.

* Wed Oct 09 2019 Simone Caronni <negativo17@gmail.com> - 1:1.16.1-1
- Update to 1.16.1.
