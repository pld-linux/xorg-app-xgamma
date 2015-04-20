Summary:	xgamma application - alter a monitor's gamma correction through X server
Summary(pl.UTF-8):	Aplikacja xgamma - zmiana korekcji gamma monitora poprzez serwer X
Name:		xorg-app-xgamma
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xgamma-%{version}.tar.bz2
# Source0-md5:	90b4305157c2b966d5180e2ee61262be
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xgamma program allows X users to query and alter the gamma correction
of a monitor via the X video mode extension
(XFree86-VidModeExtension).

%description -l pl.UTF-8
Program xgamma pozwala użytkownikom X sprawdzać i modyfikować korekcję
gamma monitora poprzez rozszerzenie X związane z trybem obrazu
(XFree86-VidModeExtension).

%prep
%setup -q -n xgamma-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xgamma
%{_mandir}/man1/xgamma.1*
