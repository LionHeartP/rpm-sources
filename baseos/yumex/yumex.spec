%global app_id dk.yumex.Yumex
%global app_build debug
%global dnf_backend DNF4
%global gitcommit 788d4453587a260f5b46a8d64863debeaf7e3984
%global shortcommit 788d445

Name:     yumex
Version:  4.99.4
Release:  0.17.git.%{shortcommit}%{?dist}
Summary:  Yum Extender graphical package management tool

Group:    Applications/System
License:  GPLv3+
URL:      http://yumex.dk
Source0:  https://github.com/timlau/yumex-ng/archive/%{gitcommit}.zip#/%{name}-%{shortcommit}.tar.gz
Source1:  dk.yumex.Yumex.svg
Patch0:   rename-desktop-shortcut.patch
Patch1:   0001-add-nobara-update-system-button.patch

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: meson
BuildRequires: blueprint-compiler >= 0.4.0
BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(pygobject-3.0)


Requires: python3-dnfdaemon
Requires: python3-gobject
Requires: python3-dnf
Requires: libadwaita
Requires: gtk4
Requires: flatpak-libs
Requires: nobara-welcome

# support for dnf5 backend
%if "%{dnf_backend}" == "DNF5"
Requires: python3-libdnf5
%endif

Obsoletes: yumex-dnf <= 4.5.1



%description
Graphical package tool for maintain packages on the system


%prep
%autosetup -n %{name}-ng-%{gitcommit} -p1
cp %{SOURCE1} ./data/icons/hicolor/scalable/apps/

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}.desktop

%build
%meson --buildtype=%{app_build} -Ddnf_backend=%{dnf_backend}
%meson_build

%install
%meson_install

%find_lang %name

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database %{_datadir}/applications &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :

%files -f  %{name}.lang
%doc README.md
%license LICENSE
%{_datadir}/%{name}
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/
%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml

%changelog

* Sat Jan 21 2023 Tim Lauridsen <timlau@fedoraproject.org> 4.99.3-1
- the 4.99.3 release

* Wed Jan 4 2023 Tim Lauridsen <timlau@fedoraproject.org> 4.99.2-1
- add support for building with dnf5 backend

* Wed Jan 4 2023 Tim Lauridsen <timlau@fedoraproject.org> 4.99.2-1
- the 4.99.2 release

* Tue Dec 20 2022 Tim Lauridsen <timlau@fedoraproject.org> 4.99.1-1
- the 4.99.1 release

* Tue Dec 20 2022 Tim Lauridsen <timlau@fedoraproject.org> 4.99.0-1
- initial release (dev)

