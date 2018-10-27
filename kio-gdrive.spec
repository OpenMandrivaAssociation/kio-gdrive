Summary: Google Drive KIO-slave for KDE applications
Name: kio-gdrive
Version: 1.2.5
Release: 1
License: GPLv2+
Group: Graphical desktop/KDE
Url: http://www.kde.org
Source0: http://download.kde.org/stable/kio-gdrive/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KPimGAPI)
BuildRequires: cmake(KAccounts)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Notifications)
BuildRequires: pkgconfig(libaccounts-glib)
BuildRequires: intltool

%description
Google Drive KIO-slave for KDE applications.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kio5_gdrive

%files -f kio5_gdrive.lang
%doc %{_docdir}/HTML/*/kioslave5/gdrive/index.*
%{_libdir}/qt5/plugins/kf5/kio/gdrive.so
%{_datadir}/remoteview/gdrive-network.desktop
%{_datadir}/metainfo/org*.xml
%{_libdir}/qt5/plugins/kaccounts/daemonplugins/gdrive.so
%{_datadir}/accounts/services/kde/google-drive.service
%{_datadir}/knotifications5/gdrive.notifyrc
