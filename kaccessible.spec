%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		kaccessible
Summary:	Accessibility services like focus tracking and a screenreader
Version:	17.04.2
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://www.kde.org/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	speech-dispatcher-devel
Obsoletes:	kdeaccessibility4-core < 2:4.8.0

%description
kaccessible implements a QAccessibleBridgePlugin to provide
accessibility services like focus tracking and a screenreader.

%files
%{_kde_libdir}/kde4/libexec/kaccessibleapp
%{_kde_libdir}/kde4/plugins/accessiblebridge/kaccessiblebridge.so
%{_datadir}/dbus-1/services/org.kde.kaccessible.service

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build
