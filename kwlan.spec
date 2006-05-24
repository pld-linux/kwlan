Summary:	KDE frontend for WPA Supplicant
Summary(pl):	Frontend kde dla WPA Supplicant.
Name:		kwlan
Version:	0.4.3
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.kde-apps.org/content/files/37041-%{name}-%{version}.tar.gz
# Source0-md5:	38f5b940dcacecc401b694db9c62d3dd
URL:		http://www.kde-apps.org/content/show.php?content=37041&PHPSESSID=e6cbfcb04852cd2c9b4ab8ac724d5a84
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	libiw-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	wpa_supplicant
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows you to configure different network profiles using all
encryptions wpa_supplicant provides (wep, wpa, wpa2 etc). Systray icon
shows connection status. Based on wpa_gui by Jouni Malinen .

%description -l pl
Pozwala na konfiguracje ró¿nych profili sieciowych, u¿ywaj±cych
wszystkich mo¿liwo¶ci, dostarczanych przez wpa supplicant. Ikona w
zasobniku systemowym pokazuje status po³±czenia. Kwlan bazuje na
wpa_gui Jouni Malinen-a.

%prep
%setup -q

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
%attr(755,root,root) %{_bindir}/kwlan
%doc AUTHORS ChangeLog README NEWS
%{_desktopdir}/kwlan.desktop
%{_datadir}/apps/kwlan/kwlanui.rc
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_iconsdir}/hicolor/*x*/apps/kwlan/*.png
