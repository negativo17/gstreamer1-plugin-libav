Name:       gstreamer1-plugin-libav
Version:    1.28.0
Release:    1%{?dist}
Epoch:      1
Summary:    GStreamer Libav plug-in
License:    LGPLv2+
URL:        https://gstreamer.freedesktop.org/modules/gst-libav.html

Source0:    https://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz

BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  libtool
BuildRequires:  meson >= 0.62
BuildRequires:  orc-devel >= 0.4.16
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavcodec) >= 58
BuildRequires:  pkgconfig(libavutil)

Obsoletes:      gstreamer1-libav < 1:1.20.3-4
Provides:       gstreamer1-libav = 1:%{version}-%{release}
Provides:       gstreamer1-libav%{?_isa} = 1:%{version}-%{release}

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
%doc ChangeLog NEWS README.md
%{_libdir}/gstreamer-1.0/libgstlibav.so

%changelog
* Mon Feb 16 2026 Simone Caronni <negativo17@gmail.com> - 1:1.28.0-1
- Update to 1.28.0.
- Trim changelog.

* Fri Jan 09 2026 Simone Caronni <negativo17@gmail.com> - 1:1.26.10-1
- Update to 1.26.10.

* Wed Dec 17 2025 Simone Caronni <negativo17@gmail.com> - 1:1.26.9-1
- Update to 1.26.9.

* Fri Nov 21 2025 Simone Caronni <negativo17@gmail.com> - 1:1.26.8-1
- Update to 1.26.8.

* Mon Oct 20 2025 Simone Caronni <negativo17@gmail.com> - 1:1.26.7-1
- Update to 1.26.7.

* Wed Sep 17 2025 Simone Caronni <negativo17@gmail.com> - 1:1.26.6-1
- Update to 1.26.6.

* Sun Aug 24 2025 Simone Caronni <negativo17@gmail.com> - 1:1.26.5-1
- Update to 1.26.5.

* Sat Jun 28 2025 Simone Caronni <negativo17@gmail.com> - 1:1.26.3-1
- Update to 1.26.3.

* Mon Jun 09 2025 Simone Caronni <negativo17@gmail.com> - 1:1.26.2-1
- Update to 1.26.2.

* Mon Apr 28 2025 Simone Caronni <negativo17@gmail.com> - 1:1.26.1-1
- Update to 1.26.1.19.

* Sun Mar 30 2025 Simone Caronni <negativo17@gmail.com> - 1:1.26.0-1
- Update to 1.26.0.

* Sat Jan 11 2025 Simone Caronni <negativo17@gmail.com> - 1:1.24.11-1
- Update to 1.24.11.
