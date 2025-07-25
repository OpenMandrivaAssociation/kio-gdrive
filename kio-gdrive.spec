#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary: Google Drive KIO-slave for KDE applications
Name: kio-gdrive
Version: 25.04.3
Release: %{?git:0.%{git}.}1
License: GPLv2+
Group: Graphical desktop/KDE
Url: https://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/network/kio-gdrive/-/archive/%{gitbranch}/kio-gdrive-%{gitbranchd}.tar.bz2#/kio-gdrive-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/kio-gdrive-%{version}.tar.xz
%endif
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KPim6GAPI)
BuildRequires: cmake(KAccounts6)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Purpose)
BuildRequires: pkgconfig(libaccounts-glib)
BuildRequires: intltool

%rename plasma6-kio-gdrive

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Google Drive KIO-slave for KDE applications.

%files -f %{name}.lang
%{_datadir}/remoteview/gdrive-network.desktop
%{_datadir}/metainfo/org*.xml
%{_qtdir}/plugins/kf6/kfileitemaction/gdrivecontextmenuaction.so
%{_qtdir}/plugins/kf6/propertiesdialog/gdrivepropertiesplugin.so
%{_qtdir}/plugins/kf6/kio/gdrive.so
%{_qtdir}/plugins/kf6/purpose/purpose_gdrive.so
%{_datadir}/purpose/purpose_gdrive_config.qml
%{_qtdir}/plugins/kaccounts/daemonplugins/gdrive.so
%{_datadir}/accounts/services/kde/google-drive.service
%{_datadir}/knotifications6/gdrive.notifyrc
