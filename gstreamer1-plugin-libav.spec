Name:       gstreamer1-plugin-libav
Version:    1.22.1
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
%doc AUTHORS NEWS README.md
%{_libdir}/gstreamer-1.0/libgstlibav.so

%changelog
* Fri Mar 17 2023 Simone Caronni <negativo17@gmail.com> - 1:1.22.1-1
- Update to 1.22.1.

* Fri Jan 20 2023 Simone Caronni <negativo17@gmail.com> - 1:1.20.5-1
- Update to 1.20.5.

* Thu Sep 15 2022 Simone Caronni <negativo17@gmail.com> - 1:1.20.3-2
- Rename to gstreamer1-plugin-libav.

* Fri Jul 22 2022 Simone Caronni <negativo17@gmail.com> - 1:1.20.3-1
- Update to 1.20.3.
- Trim changelog.

* Fri Apr 08 2022 Simone Caronni <negativo17@gmail.com> - 1:1.20.0-2
- Rebuild for updated dependencies.

* Wed Feb 09 2022 Simone Caronni <negativo17@gmail.com> - 1:1.20.0-1
- Update to 1.20.0.

* Mon Nov 15 2021 Simone Caronni <negativo17@gmail.com> - 1:1.19.3-1
- Update to 1.19.3.

* Sun Oct 24 2021 Simone Caronni <negativo17@gmail.com> - 1:1.19.2-1
- Update to 1.19.2.

* Wed Sep 22 2021 Fabio Valentini <decathorpe@gmail.com> - 1:1.19.1-1
- Update to 1.19.1.

* Mon Apr 12 2021 Simone Caronni <negativo17@gmail.com> - 1:1.18.4-1
- Update to 1.18.4.

* Thu Jan 14 2021 Simone Caronni <negativo17@gmail.com> - 1:1.18.2-1
- Update to 1.18.2.
