Summary: Google Drive KIO-slave for KDE applications
Name: plasma6-kio-gdrive
Version: 24.01.90
Release: 1
License: GPLv2+
Group: Graphical desktop/KDE
Url: http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/kio-gdrive-%{version}.tar.xz
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KPim6GAPI)
BuildRequires: cmake(KAccounts)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Purpose)
BuildRequires: pkgconfig(libaccounts-glib)
BuildRequires: intltool

%description
Google Drive KIO-slave for KDE applications.

%prep
%autosetup -p1 -n kio-gdrive-%{?git:master}%{!?git:%{version}}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kio5_gdrive

%files -f kio5_gdrive.lang
%doc %{_docdir}/HTML/*/kioslave5/gdrive/index.*
%{_datadir}/remoteview/gdrive-network.desktop
%{_datadir}/metainfo/org*.xml
%{_qtdir}/plugins/kf6/kfileitemaction/gdrivecontextmenuaction.so
%{_qtdir}/plugins/kf6/propertiesdialog/gdrivepropertiesplugin.so
%{_qtdir}/plugins/kf6/kio/gdrive.so
%{_qtdir}/plugins/kf6/purpose/purpose_gdrive.so
%{_datadir}/purpose/purpose_gdrive_config.qml
