#
# Conditional build:
%bcond_with	epistrophy	# ???
#
Summary:	Small window manager
Summary(pl.UTF-8):	Mały zarządca okien dla X Window
Name:		swm
Version:	1.3.4
Release:	3
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.small-window-manager.de/%{name}-%{version}-src.tgz
# Source0-md5:	70df4f59ee8584bb3f11056c1ade1d9b
Source1:	%{name}-xsession.desktop
Patch0:		%{name}-make.patch
Patch1:		%{name}-amd64.patch
URL:		http://www.small-window-manager.de/
BuildRequires:	XFree86-devel
BuildRequires:	rpm-build >= 4.0.2-48
%{?with_epistrophy:Requires:	epistrophy}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sWM is a very small and fast window manager for the X Window System.
It should run under any version of Linux, BSD, UNIX and other
compatible operating systems. It is designed to be fast and efficient
and even runs on Linux-PDAs such as the Compaq iPAQ. If you use it on
a rather unusual or exotic plattform please *please* send me a mail so
your system can be listed. :-) sWM was tested under: Linux Mandrake
8.1, Linux Mandrake 8.0, RedHat 6.0, Debian 2.0.

%description -l pl.UTF-8
sWM jest bardzo małym i szybkim zarządcą okien dla X Window System.
Powinien działać pod dowolną wersją Linuksa, BSD, UNIX i innych
zgodnych z nimi systemów. sWM został zaprojektowany by działać
efektywnie nawet na Linux-PDA takich jak Compaq iPAQ. Jeżeli używasz
go na jakiejś egzotycznej platformie proszę *proszę* przyślij
wiadomość e-mail, to i Twój system zostanie tu wymieniony. sWM był
testowany na Linuksach: Mandrake 8.1, Mandrake 8.0, RedHat 6.0, Debian
2.0.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__make} -C src -f Makefile-xpm \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%{__make} -C swmswitch \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%{__make} -C swmbg \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/{%{name},xsessions}} \
	$RPM_BUILD_ROOT%{_mandir}/{man1,de/man1}

install src/startswm $RPM_BUILD_ROOT%{_bindir}
install src/swm $RPM_BUILD_ROOT%{_bindir}
install swmswitch/swmswitch $RPM_BUILD_ROOT%{_bindir}

install src/swm.1x $RPM_BUILD_ROOT%{_mandir}/man1
install swmswitch/swmswitch.1x $RPM_BUILD_ROOT%{_mandir}/man1
install swmbg/swmbg.1x $RPM_BUILD_ROOT%{_mandir}/man1
install src/swm-de.1x $RPM_BUILD_ROOT%{_mandir}/de/man1/swm.1x
install swmbg/swmbg-de.1x $RPM_BUILD_ROOT%{_mandir}/de/man1/swmbg.1x

cp -rdp share/swm $RPM_BUILD_ROOT%{_datadir}
cp -rdp swmbg/pixmaps $RPM_BUILD_ROOT%{_datadir}/swm

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
