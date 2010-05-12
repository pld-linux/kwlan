Summary:	KDE frontend for WPA Supplicant
Summary(pl.UTF-8):	Frontend KDE dla programu WPA Supplicant
Name:		kwlan
Version:	0.6.3
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/kwlan/%{name}-%{version}.tar.bz2
# Source0-md5:	878f4a81aed8db736a6a89b4aa12e781
Patch0:		%{name}-desktop.patch
URL:		http://www.kde-apps.org/content/show.php?content=37041
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.0.3
BuildRequires:	libiw-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	wpa_supplicant
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows you to configure different network profiles using all
encryptions wpa_supplicant provides (WEP, WPA, WPA2 etc). Systray icon
shows connection status. Based on wpa_gui by Jouni Malinen.

%description -l pl.UTF-8
kwlan pozwala na konfigurację różnych profili sieciowych przy użyciu
wszystkich metod szyfrowania udostępnianych przez program
wpa_supplicant (WEP, WPA, WPA2 itp.). Ikona w zasobniku systemowym
pokazuje status połączenia. kwlan jest oparty na wpa_gui Jouni
Malinena.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir} \
	--with-qt-includes=%{_includedir}/qt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde --all-name
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/kwlan
%{_desktopdir}/kwlan.desktop
%{_datadir}/apps/kwlan
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_iconsdir}/hicolor/*x*/apps/kwlan
