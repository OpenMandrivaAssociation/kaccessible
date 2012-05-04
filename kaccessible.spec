Name:    kaccessible
Summary: Accessibility services like focus tracking and a screenreader
Version: 4.8.3
Release: 1
Group:   Graphical desktop/KDE
License: LGPLv2
URL:     http://www.kde.org/
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/%{name}-%version.tar.xz

BuildRequires: kdelibs4-devel >= 2:%{version}
Obsoletes: kdeaccessibility4-core

%description
kaccessible implements a QAccessibleBridgePlugin to provide 
accessibility services like focus tracking and a screenreader.

%files
%_kde_libdir/kde4/libexec/kaccessibleapp
%_kde_libdir/kde4/plugins/accessiblebridge/kaccessiblebridge.so
%_datadir/dbus-1/services/org.kde.kaccessible.service

#----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
	
%make

%install
%makeinstall_std -C build

