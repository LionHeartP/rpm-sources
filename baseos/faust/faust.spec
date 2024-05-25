# Tag: Jack, Alsa
# Type: Standalone, Language
# Category: Audio, Programming

Name:	 faust
Version: 2.69.3
Release: 37%{?dist}
Summary: Compiled language for real-time audio signal processing
# Examples are BSD
# The rest is GPLv2+
License: GPLv2+ and BSD
URL:     http://faust.grame.fr

Vendor:       Audinux
Distribution: Audinux

# to get source:
# ./faust-source.sh 2.69.3

Source0: faust.tar.gz
Source1: faust-backends.cmake
Source2: faust-source.sh

BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: cmake
BuildRequires: unzip
BuildRequires: pandoc
BuildRequires: python2
BuildRequires: texlive-latex
BuildRequires: texlive-collection-basic
BuildRequires: texlive-collection-fontsrecommended
BuildRequires: texlive-mdwtools
BuildRequires: libmicrohttpd-devel
%if 0%{?fedora} < 39
BuildRequires: llvm-devel
%else
BuildRequires: llvm16-devel
%endif
%description
Faust AUdio STreams is a functional programming language for real-time audio
signal processing. Its programming model combines two approaches : functional
programming and block diagram composition. You can think of FAUST as a
structured block diagram language with a textual syntax.

FAUST is intended for developers who need to develop efficient C/C++ audio
plugins for existing systems or full standalone audio applications. Thanks to
some specific compilation techniques and powerful optimizations, the C++ code
generated by the Faust compiler is usually very fast. It can generally compete
with (and sometimes outperform) hand-written C code.

Programming with FAUST is somehow like working with electronic circuits and
signals. A FAUST program is a list of definitions that defines a signal
processor block-diagram : a piece of code that produces output signals
according to its input signals (and maybe some user interface parameters)

%package doc
Summary: Documentation for %{name}
License: GPL-2.0-or-later
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description doc
Faust AUdio STreams is a functional programming language for real-time audio
signal processing. This package provides documentation files to help with
writing programs with faust.

%package osclib
Summary: OSCLib Library
License: GPLv2+ and MIT
Requires: %{name} = %{version}-%{release}

%description osclib
Faust AUdio STreams is a functional programming language for real-time audio
signal processing. This package provides osclib.

%package osclib-devel
Summary: Headers for the OSCLib Library
License: GPLv2+ and MIT
Requires: %{name}-osclib = %{version}-%{release}

%description osclib-devel
Faust AUdio STreams is a functional programming language for real-time audio
signal processing. This package provides the development files for osclib.

%package tools
Summary: 3rd party tools written for %{name}
License: GPL-2.0-or-later
BuildArch: noarch
Requires: %{name}-osclib-devel = %{version}-%{release}
Requires: python3
Requires: ruby

%description tools
Faust AUdio STreams is a functional programming language for real-time audio
signal processing. These additional tools are provided by various contributors
to help the building process of applications and plugins with Faust.

%package kate
Summary: Kate/Kwrite plugin for %{name}
License: GPL-2.0-or-later
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description kate
Faust AUdio STreams is a functional programming language for real-time audio
signal processing. This package provides Faust code syntax highlighting support
for KDE's Kate/Kwrite.

%package stdlib
Summary: standard libraries for %{name}
License: GPL-2.0-or-later
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description stdlib
Faust AUdio STreams is a functional programming language for real-time audio
signal processing. These libraries are part of the standard Faust libraries.

%prep
%autosetup -n faust

cp %{SOURCE1} build

%build

%if 0%{?fedora} >= 39
export PATH=$PATH:/usr/lib64/llvm16/bin
%endif

%set_build_flags
cd build
%cmake -DINCLUDE_DYNAMIC=ON \
       -DLIBSDIR=%{_lib} \
       -C %{SOURCE1} \
%if 0%{?fedora} >= 38
    -DCMAKE_CXX_FLAGS="-include cstdint -fPIC $CXXFLAGS"
%endif
%cmake_build

%install

cd build
%cmake_install

# cleanup
rm -f %{buildroot}/%{_libdir}/ios-libsndfile.a
rm -f %{buildroot}/%{_datadir}/%{name}/android/app/lib/libsndfile/lib/arm64-v8a/libsndfile.so
rm -f %{buildroot}/%{_datadir}/%{name}/android/app/lib/libsndfile/lib/armeabi-v7a/libsndfile.so
rm -f %{buildroot}/%{_datadir}/%{name}/max-msp/sndfile/arm/libsndfile.a
rm -f %{buildroot}/%{_datadir}/%{name}/max-msp/sndfile/intel/libsndfile.a

# Fix usage.sh
mv %{buildroot}/%{_bindir}/usage.sh %{buildroot}/%{_datadir}/%{name}/
for Files in `grep -lr usage.sh %{buildroot}/%{_bindir}/`
do
  sed -i -e "s|usage.sh|%{_datadir}/%{name}/usage.sh|g" $Files
done

%files
%doc README.md examples
%license COPYING.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/*

%files osclib
%doc architecture/osclib/README.md
%{_libdir}/*.so.*

%files osclib-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a

%files doc
%doc documentation/*

%files tools
%doc tools/README.md tools/%{name}2pd
%{_bindir}/%{name}2*
%{_bindir}/encoderunitypackage
%{_bindir}/faustoptflags
%{_bindir}/faustpath
%{_bindir}/sound2reader
%{_bindir}/filename2ident
%{_bindir}/faustremote
%{_bindir}/faust-config

%files stdlib
%{_datadir}/faust/*.lib

%changelog
* Mon Nov 13 2023 Yann Collette <ycollette.nospam@free.fr> - 2.69.3-37
- update to 2.69.3-37

* Tue Sep 19 2023 Yann Collette <ycollette.nospam@free.fr> - 2.68.1-37
- update to 2.68.1-37

* Sat Jun 17 2023 Yann Collette <ycollette.nospam@free.fr> - 2.68.0-37
- update to 2.68.0-37

* Sat Jun 17 2023 Yann Collette <ycollette.nospam@free.fr> - 2.60.3-37
- update to 2.60.3-37

* Mon May 15 2023 Yann Collette <ycollette.nospam@free.fr> - 2.59.6-37
- update to 2.59.6-37

* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 2.59.5-37
- update to 2.59.5-37

* Sun Mar 26 2023 Yann Collette <ycollette.nospam@free.fr> - 2.54.9-37
- update to 2.54.9-37 - enable some other backends

* Tue Mar 07 2023 Yann Collette <ycollette.nospam@free.fr> - 2.54.9-36
- update to 2.54.9-36 - use cmake to build

* Tue Oct 04 2022 Yann Collette <ycollette.nospam@free.fr> - 2.50.6-25
- update to 2.50.6-25

* Wed Sep 28 2022 Yann Collette <ycollette.nospam@free.fr> - 2.41.1-25
- update to 2.41.1-25 - fixes for f37

* Mon Jul 18 2022 Yann Collette <ycollette.nospam@free.fr> - 2.41.1-24
- update to 2.41.1-24

* Thu Jun 30 2022 Yann Collette <ycollette.nospam@free.fr> - 2.41.1-23
- update to 2.41.1-23

* Mon Nov 01 2021 Yann Collette <ycollette.nospam@free.fr> - 2.37.3-23
- update to 2.37.3-23

* Wed Jul 21 2021 Yann Collette <ycollette.nospam@free.fr> - 2.33.1-23
- update to 2.33.1-23

* Sat Jan 23 2021 Yann Collette <ycollette.nospam@free.fr> - 2.30.5-23
- update to 2.30.5-23

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 2.27.2-23
- fix debug build

* Mon Aug 17 2020 Yann Collette <ycollette.nospam@free.fr> - 2.27.2-22
- Update to 2.27.2-22. Fix python in faust2appl tools

* Thu Aug 6 2020 Yann Collette <ycollette.nospam@free.fr> - 2.27.2-21
- Update to 2.27.2-21.

* Wed Jul 22 2020 Yann Collette <ycollette.nospam@free.fr> - 2.27.1-21
- Update to 2.27.1-21. Fix install

* Tue Jul 21 2020 Yann Collette <ycollette.nospam@free.fr> - 2.27.1-20
- Update to 2.27.1-20

* Tue May 12 2020 Yann Collette <ycollette.nospam@free.fr> - 2.20.2-20
- Update to 2.20.2-20. Fix libraries installation

* Sat Apr 25 2020 Yann Collette <ycollette.nospam@free.fr> - 2.20.2-19
- Update to 2.20.2-19.

* Wed Apr 22 2020 Yann Collette <ycollette.nospam@free.fr> - 2.14.4-19
- Update to 2.14.4-19. Fix for Fedora 32

* Wed Jan 15 2020 Yann Collette <ycollette.nospam@free.fr> - 2.14.4-18
- Update to 2.14.4-18. Add stdlib

* Mon Jan 13 2020 Yann Collette <ycollette.nospam@free.fr> - 2.14.4-17
- Update to 2.14.4-17

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.46-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.46-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.46-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.46-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.46-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.46-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.46-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.46-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 10 2016 Jon Ciesla <limburgher@gmail.com> - 0.9.46-9
- Drop kdesdk Requires, retired.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.46-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.46-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.46-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.46-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 31 2012 Jon Ciesla <limburgher@gmail.com> - 0.9.46-1
- New upstream.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.43-4
- Rebuilt for c++ ABI breakage

* Tue Jan 10 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.43-3
- gcc-4.7 compile fix

* Sun Nov 27 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.43-2
- Drop executable permission on faust2pd.pure to avoid an unavailable dependency.

* Fri Nov 25 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.43-1
- Update to 0.9.43

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.30-1
- Update to 0.9.30

* Mon May 31 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.24-1
- Update to 0.9.24
- Don't bundle the source documentation. It is only needed by faust developers, not users.

* Sat May 15 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.22-1
- Update to 0.9.22

* Sun Jan 31 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.10-1
- Update to 0.9.10

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.4-3.b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 21 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.9.4-2.b
- Fix the year of the previous changelog entry
- Install the nonbinary files in %%{_datadir}/%%{name}/
- Add Requires: %%{name}=%%{version}-%%{release} to the doc subpackage

* Mon Mar 16 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.9.4-1.b
- Initial build