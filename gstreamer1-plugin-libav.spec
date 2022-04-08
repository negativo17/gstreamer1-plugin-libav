Name:       gstreamer1-plugin-libav
Version:    1.18.4
Release:    2%{?dist}
Epoch:      1
Summary:    GStreamer Libav plug-in
License:    LGPLv2+
URL:        https://gstreamer.freedesktop.org/modules/gst-libav.html

Source0:    http://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz

BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  libtool
BuildRequires:  meson >= 0.48.0
BuildRequires:  orc-devel >= 0.4.16
# FFMpeg 4.4.x:
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

%prep
%autosetup -p1 -n gst-libav-%{version}

%build
#export CFLAGS="%{optflags} -Wno-error=attributes"
%meson \
  -D package-name="Fedora GStreamer-plugins-ugly package" \
  -D package-origin="https://negativo17.org" \
  -D doc=disabled
%meson_build

%install
%meson_install
find %{buildroot} -name "*.la" -delete

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md
%{_libdir}/gstreamer-1.0/libgstlibav.so

%changelog
* Fri Feb 10 2023 Simone Caronni <negativo17@gmail.com> - 1:1.18.4-2
- First build for el9.

* Mon Apr 12 2021 Simone Caronni <negativo17@gmail.com> - 1:1.18.4-1
- Update to 1.18.4.

* Thu Jan 14 2021 Simone Caronni <negativo17@gmail.com> - 1:1.18.2-1
- Update to 1.18.2.

* Sun Nov 01 2020 Simone Caronni <negativo17@gmail.com> - 1:1.18.1-1
- Update to 1.18.1, rebase on Meson.
- Trim changelog.

* Mon Jun 29 2020 Simone Caronni <negativo17@gmail.com> - 1:1.16.2-2
- Rebuild for updated dependencies.

* Tue Feb 11 2020 Simone Caronni <negativo17@gmail.com> - 1:1.16.2-1
- Update to 1.16.2.
