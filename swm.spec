Summary:	Small window manager
Summary(pl):	Ma³y zarz±dca okien dla X Window
Name:		swm
Version:	1.3.4
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.small-window-manager.de/%{name}-%{version}-src.tgz
Patch0:		%{name}-make.patch
URL:		http://www.small-window-manager.de/
BuildRequires:	XFree86-devel
BuildRequires:	rpm-build >= 4.0.2-48
%{?_with_epistrophy:Requires:	epistrophy}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/%{name}

%description
sWM is a very small and fast window manager for the X Window System.
It should run under any version of Linux, BSD, UNIX and other
compatible operating systems. It is designed to be fast and efficient
and even runs on Linux-PDAs such as the Compaq iPAQ. If you use it on
a rather unusual or exotic plattform please *please* send me a mail so
your system can be listed. :-) sWM was tested under: Linux Mandrake
8.1, Linux Mandrake 8.0, RedHat 6.0, Debian 2.0.

%description -l pl
sWM jest bardzo ma³ym i szybkim zarz±dc± okien dla X Window. Powinien
dzia³aæ pod dowoln± wersj± Linuksa, BSD, UNIX i innych zgodnych z nimi
systemów. sWM zosta³ zaprojektowany by dzia³aæ efektywnie nawet na
Linux-PDA takich jak Compaq iPAQ. Je¿eli u¿ywasz go na jakiej¶
egzotycznej platformie proszê *proszê* przy¶lij wiadomo¶æ e-mail, to i
Twój system zostanie tu wymieniony. sWM by³ testowany na: Linux
Mandrake 8.1, Linux Mandrake 8.0, RedHat 6.0, Debian 2.0.

%prep
%setup -q
%patch0 -p1

%build
cd src
%{__make} -f Makefile-xpm CFLAGS="%{rpmcflags} %{rpmldflags}"
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/usr/share/swm,%{_mandir}/{man1,de/man1}}

cd src
%{__make} -f Makefile-xpm install DESTDIR=$RPM_BUILD_ROOT
cd ..

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/
%attr(755,root,root) %{_bindir}/*
%dir /usr/share/swm
/usr/share/swm/*
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
