%global appname org.gnome.Characters

Name:		gnome-characters
Version:	3.28.2
Release:	1%{?dist}
Summary:	Character map application for GNOME
# Files from gtk-js-app are licensed under 3-clause BSD.
# Other files are GPL 2.0 or later.
License:	BSD and GPLv2+
URL:		https://wiki.gnome.org/Design/Apps/CharacterMap
Source0:	https://download.gnome.org/sources/gnome-characters/3.28/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
# This package uses GtkWidget template, which was added in Gjs 1.43.3.
BuildRequires:	gjs-devel >= 1.43.3
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk3-devel
BuildRequires:	libappstream-glib
BuildRequires:	libunistring-devel
BuildRequires:	meson
Requires:	gjs >= 1.43.3

%description
Characters is a simple utility application to find and insert unusual
characters.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{appname}


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/%{appname}.desktop


%files -f %{appname}.lang
%doc NEWS
%license COPYING COPYINGv2
%{_bindir}/%{name}
%{_datadir}/dbus-1/services/%{appname}.BackgroundService.service
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}-symbolic.svg
%{_datadir}/%{appname}
%{_datadir}/gnome-shell/search-providers/%{appname}.search-provider.ini
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_libdir}/%{appname}


%changelog
* Tue May 08 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92
- Switch to the meson build system
- Build with system libunistring

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.2-2
- Remove obsolete scriptlets

* Wed Nov 01 2017 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Thu Sep 07 2017 Kalev Lember <klember@redhat.com> - 3.25.92-1
- Update to 3.25.92

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 21 2016 Daiki Ueno <dueno@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Sat Aug 27 2016 Kalev Lember <klember@redhat.com> - 3.21.91.1-1
- Update to 3.21.91.1

* Wed Apr 13 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Mon Mar 14 2016 Kalev Lember <klember@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Sun Oct 11 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Fri Oct 09 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.18.0-3
- Disable the search provider by default.

* Tue Sep 29 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.18.0-2
- Add symbolic icon and X-GNOME-Utilities desktop category.

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Aug 31 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Fri Aug 21 2015 Matthias Clasen <mclasen@redhat.com> - 3.17.90-2
- Force-update the icon cache for the gnome theme. This is necessary
  because icons were moved from gnome to hicolor, and if we don't update
  the gnome icon cache, it hides the icons in lower hicolor theme.
  This is a one-shot fix, and should be removed in the next package
  update.

* Tue Aug 18 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90

* Wed Jul 29 2015 Daiki Ueno <dueno@redhat.com> - 3.17.4.1-1
- Update to 3.17.4.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2-1
- Update to 3.16.2

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Daiki Ueno <dueno@redhat.com> - 3.15.92-1
- Initial packaging for Fedora
